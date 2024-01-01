# %%time

# from tqdm import notebook

import os
import pandas as pd
from datetime import datetime
import glob

class Globbing_file:        
    
    def __init__(self, path, ext, start_idx, end_idx, save_num, folder_depth, file_encoding):
        self._path = path
        if ext == '*':
            self._ext = 'all'
        else:
            self._ext = ext
        self._start_idx = start_idx
        self._end_idx = end_idx
        self._save_num = save_num
        self._folder_depth = folder_depth
        self._file_encoding = file_encoding
        self._result_df = pd.DataFrame()

            
    # Getter 및 Setter 정의
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def ext(self):
        return self._ext

    @ext.setter
    def ext(self, value):
        self._ext = value

    @property
    def start_idx(self):
        return self._start_idx

    @start_idx.setter
    def start_idx(self, value):
        self._start_idx = value

    @property
    def end_idx(self):
        return self._end_idx

    @end_idx.setter
    def end_idx(self, value):
        self._end_idx = value

    @property
    def save_num(self):
        return self._save_num

    @save_num.setter
    def save_num(self, value):
        self._save_num = value

    @property
    def folder_depth(self):
        return self._folder_depth

    @folder_depth.setter
    def folder_depth(self, value):
        self._folder_depth = value
        
    @property
    def file_encoding(self):
        return self._file_encoding

    @file_encoding.setter
    def file_encoding(self, value):
        self._file_encoding = value 

    @property
    def result_df(self):
        return self._result_df

    @result_df.setter
    def result_df(self, value):
        self._result_df = value        
    
    def file_name_def(self):
        return f'{self.ext}_file_list.csv'

    # 지정한 폴더 하위 경로의 폴더, 파일 모두 불러온 뒤, 선택한 확장자가 존재하는 파일 리스트 추출 
    def file_folder_list_save(self, f_list, f_ctg):
        try:
            file_name = self.file_name_def()
            print(f'{f_ctg} 개수 확인 : {len(f_list)}')
            f_list_df = pd.DataFrame(f_list)
            if f_ctg != self.ext:
                current_time = datetime.now().strftime("%y%m%d_%H%M")
                f_list_df.to_csv(f'{f_ctg}_{current_time}.csv')
            else:
                f_list_df.to_csv(file_name)
            print(f'{f_ctg} 리스트 생성 완료')
        except Exception as e:
            print(f'에러 : {str(e)}')

    def file_folder_list_load(self):
        try:            
            # 이미 저장된 파일리스트가 존재한다면 해당 파일 리스트를 불러오고 없으면 새로 저장
            file_name = self.file_name_def()
            if os.path.exists(file_name):
                file_list_df = pd.read_csv(file_name)
                if file_list_df.empty:
                    file_list = []
                else:
                    file_list = file_list_df.iloc[:,1].tolist()
                print(f'{file_name} 로딩 완료')
            else:
                file_folder_list = glob.glob(self.path + '/**', recursive=True)
                self.file_folder_list_save(file_folder_list, 'all')

                folder_list = [folder_path for folder_path in notebook.tqdm(file_folder_list) if os.path.isdir(folder_path)]
                self.file_folder_list_save(folder_list, 'folder')

                file_list = [file_path for file_path in notebook.tqdm(file_folder_list) if file_path not in folder_list]
                self.file_folder_list_save(file_list, 'file')                
                                                
                # 확장자가 self.ext 인 파일만 선택해서 리스트 생성 : 탐색 시간이 너무 오래걸려서 보류 # file_list에서 slice 해서 사용
                # ext_file_list = [file_path for file_path in notebook.tqdm(file_list, desc=f'{self.ext} 리스트 생성중') if file_path.endswith(f'.{self.ext}') in file_list]
                # self.file_folder_list_save(ext_file_list, self.ext)
                  
            return file_list

        except Exception as e:
            print(f'에러 : {str(e)}')

    def file_name_save(self, file):
        try:
            # 폴더 경로 깊이 파일을 기준으로 folder_depth 까지 폴더명을 파일명으로 저장, -1 은 파일명임
            folder = os.path.dirname(file).split(os.sep)        
            if len(folder) >= abs(self.folder_depth):
                file_name_parts = [folder[i - self.folder_depth] for i in range(len(folder)) if i >= self.folder_depth]
                file_name_root = '_'.join(file_name_parts)
            else:
                file_name_parts = ''
                            
            return file_name_root

        except Exception as e:
            print(f'에러 : {str(e)}')

    def mid_file_save(self, file_name_root, lis):
        try:
            # ext에 * 와이드 카드 입력시 파일명 save 에러, if else 넣기 귀찮아서 주석처리
            # save_path = f'./{file_name_root}_{self.ext}_list' 
            save_path = f'./{file_name_root}_list'

            # 알파벳, 숫자, 언더스코어('_'), 대시('-')만 남기도록 수정
            # save_path = ''.join(c for c in save_path if c.isalnum() or c in ['_', '-'])
            os.makedirs(save_path, exist_ok=True)

            i = len(lis)
            # save_num 개마다 csv 파일 생성
            if (i % self.save_num) == 0:
                j = i - self.save_num                
                mid_df = pd.concat(lis[j:i], axis=0, ignore_index=True)

                # 현재 시각으로 파일 저장
                current_time = datetime.now().strftime("%y%m%d_%H%M")
                mid_file_path = f'{save_path}/{file_name_root}_list_[{j}-{i}]_{current_time}.csv'
                mid_df.to_csv(mid_file_path, encoding=self.file_encoding)
                print(f'{mid_file_path} 생성 완료')
                j = i
            else:
                pass

        except Exception as e:
            print(f'에러 : {str(e)}')

    def final_file_save(self, final_file_list_df, file_name_root, lis):
        try:
            # 현재 시각으로 파일 저장
            current_time = datetime.now().strftime("%y%m%d_%H%M")
            final_file_path = f'{file_name_root}_final_list_[{self.start_idx}-{self.end_idx}]_{current_time}.csv'
            final_file_list_df.to_csv(final_file_path, encoding=self.file_encoding)
            print(f'{final_file_path} 생성 완료')
            final_file_list_df.info()

            # 시작3개, 마지막3개 / 저장된 파일리스트 검증 확인용
            print(final_file_list_df[:3])
            print(final_file_list_df[-3:])
            return final_file_list_df   

        except Exception as e:
            print(f'에러 : {str(e)}')

    def file_list_save(self):
        try:
            print(f'시작 인덱스 : {self.start_idx}\n마지막 인덱스 : {self.end_idx}')
            print(f'glob 경로 : {self.path}')
            file_list = self.file_folder_list_load()
            return file_list
        except Exception as e:
            print(f'에러 : {str(e)}')
                        

    def file_list_extract(self, file_list):        
        try:                        
            lis = []
            i = 0

            print()
            print(f'{self.ext} 추출 중')
            
            if self.ext == 'json':
                for file in notebook.tqdm(file_list[self.start_idx : self.end_idx], desc=f'{self.ext} 추출 중'):
                    df = pd.read_json(file, encoding='utf-8-sig')
                    json = pd.concat([df.iloc[:7, 0], df.iloc[7:, 1]])
                    lis.append(json)                                        
                    file_name_root = self.file_name_save(file)                                    
                    self.mid_file_save(file_name_root, lis)
                final_file_list_df = pd.concat(lis, axis=1).T
                    
            elif self.ext == 'csv':
                for file in notebook.tqdm(file_list[self.start_idx : self.end_idx], desc=f'{self.ext} 추출 중'):
                    csv = pd.read_csv(file, encoding='cp949') # euc-kr     
                    lis.append(csv)                    
                    file_name_root = self.file_name_save(file)                                    
                    self.mid_file_save(file_name_root, lis)
                final_file_list_df = pd.concat(lis, axis=0, ignore_index=True)

            print(f'{self.ext} 추출 완료\n\nDataFrame 생성중')

            result_df = self.final_file_save(final_file_list_df, file_name_root, lis)

            return result_df

        except Exception as e:
            print(f'에러 : {str(e)}')


            
# 사용자 입력 컨텍스트
context = {
    'path' : 'C:/FINAL_PROJECT/farm_quest_data/data/104.식물 병 유발 통합 데이터',

    # 불러올 파일 확장자 # * 와이들 카드 모든 파일 탐색 
    'ext': 'csv',

    # 슬라이싱 인덱스 # json ~547955 / csv 547955~
    'start_idx' : 547955,
    'end_idx' : -1,

    # csv 로 저장시킬 파일 묶음 단위
    'save_num' : 20000,

    # 파일명 가장 앞에 넣을 폴더 경로 깊이 (파일 기준 -인덱스) : json(-7) / csv(-6)
    'folder_depth' : -6,
    
    # 저장할 파일 인코더 : 파일 메모장으로 열어서 새 이름으로 저장 후 인코딩 확인 json : 'utf-8-sig' / csv : 'cp949' 
    'file_encoding' : 'cp949',
    
}

# 인스턴스 생성
glob_file = Globbing_file(
    path=context['path'],
    ext=context['ext'],
    start_idx=context['start_idx'],
    end_idx=context['end_idx'],
    save_num=context['save_num'],
    folder_depth=context['folder_depth'],
    file_encoding=context['file_encoding'],
)

# 파일 리스트 생성 (csv 형태로 저장 동시 진행)
file_list = glob_file.file_list_save()

# 데이터프레임 반환
file_glob_df = glob_file.file_list_extract(file_list)
file_glob_df[:1]

