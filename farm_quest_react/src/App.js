import './App.css';
import logo from './logo.svg';

import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from "react-router-dom";

// 고객센터
import { CSNotice, CSFAQ, CS1vs1 } from './cs_content';



// function Home() {
//   return <div> 홈</div>;
// }

function Login() {
  return <div>로그인</div>;
}

function Signup(){
  return (<div> 회원가입</div>);
}

function Logout() {
  return (<div> 로그아웃</div>);
}

function CsBoard() {
  return (<div> 고객센터</div>);
}


function App() {
  const [selectedComponent, setSelectedComponent] = useState(null);

  const showComponent = (componentName) => {
    setSelectedComponent(componentName);
  };

  return (
    // App 컴포넌트 시작
    <div className="App">

      {/* 헤더 컴포넌트 시작 */}
      <header className="App-header">
        <div class="site_logo"><img src={logo} className="App-logo" alt="logo" /></div>
        <a href="/"><div class="site_home">팜 퀘스트</div></a>
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
        <div class="header_menu">
          <Router>            
            {/* <Link to = "/">홈 </Link> */}
            <Link to = "/CsBoard">고객센터 </Link> 
            <Link to = "/signup">회원가입 </Link> 
            <Link to = "/login">로그인 </Link> 
            <Link to = "/logout">로그아웃 </Link>
            
            <Routes>
              {/* <Route exact path="/" element={<Home/>}/>               */}
              <Route path="/CsBoard" element={<CsBoard/>}/>
              <Route path="/signup" element={<Signup/>}/>
              <Route path="/login" element={<Login/>}/>                
              <Route path="/logout" element={<Logout/>}/>
                
            </Routes>
          </Router>        
        </div>

        {/* 네비게이션 컴포넌트 시작 */}
        <nav class="root_nav">          
          <div>nav_content</div>
        
        </nav>
        {/* 네비게이션 컴포넌트 끝 */}
      
      </header>
      {/* 헤더 컴포넌트 끝 */}

      {/* 카테고리 상세 컨텐트 박스 시작 */}      
      <div className={`ctg_content ${selectedComponent ? 'cs_layout' : ''}`}>
        
        {/* 고객센터 게시판 컴포넌트 시작 */}
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
            {selectedComponent === "cs_notice" && <CSNotice />}
            {selectedComponent === "cs_faq" && <CSFAQ />}
            {selectedComponent === "cs_1vs1" && <CS1vs1 />}
          </div>
        </section>
        {/* 고객센터 컴포넌트 끝 */}

      </div>
      {/* 카테고리 상세 컨텐츠 박스 끝 */}

    </div>
    // App 컴포넌트 끝

  );
}



export default App;
