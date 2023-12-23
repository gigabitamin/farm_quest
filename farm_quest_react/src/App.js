// import logo from './logo.svg';
import './App.css';

import React, { useState } from 'react';
import { CSNotice, CSFAQ, CS1vs1 } from './cs_content';



function App() {
  const [selectedComponent, setSelectedComponent] = useState(null);

  const showComponent = (componentName) => {
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
          {selectedComponent === "cs_notice" && <CSNotice />}
          {selectedComponent === "cs_faq" && <CSFAQ />}
          {selectedComponent === "cs_1vs1" && <CS1vs1 />}
        </div>
      </section>      
    </div>
  );
}

export default App;
