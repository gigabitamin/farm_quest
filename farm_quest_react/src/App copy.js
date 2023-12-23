// import logo from './logo.svg';
import './App.css';

import React, { useState } from 'react';
import { CSNotice, CSFAQ, CS1vs1 } from './cs_content';



function App() {

  const [selectedComponent, setSelectedComponent] = useState(null);

  const showComponent = (componentName) => {
    // 클릭된 메뉴에 따라 보여줄 컴포넌트를 설정
    setSelectedComponent(componentName);
  };


  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}            
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}

      <h1>고객 센터</h1>
      </header>
      <section class="cs_layout">
        <div class="cs_sidebar">
          <div class="cs_menu">
            <div onClick={() => showComponent("cs_notice")} className="cs_notice">
              공지사항
            </div>
            <div onClick={() => showComponent("cs_faq")} className="cs_faq">
              FAQ
            </div>
            <div onClick={() => showComponent("cs_1vs1")} className="cs_1vs1">
              1:1 문의
            </div>
          </div>
        </div>
        <div class="cs_content_area">cs_content_area
          {selectedComponent === "cs_notice" && (
            <div className="cs_content">cs_notice 컴포넌트 내용</div>
          )}
          {selectedComponent === "cs_faq" && (
            <div className="cs_content">cs_faq 컴포넌트 내용</div>
          )}
          {selectedComponent === "cs_1vs1" && (
            <div className="cs_content">cs_1vs1 컴포넌트 내용</div>
          )}
        </div>
      </section>      
    </div>
  );
}

export default App;
