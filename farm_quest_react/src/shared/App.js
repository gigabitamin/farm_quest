import React, { Component } from "react";
import { Routes, Route } from "react-router-dom";
import {
  Main,
  Like,
  My,
  Login,
  Detail,
  Register,
  New,
  Profile,
} from "../pages/index";
import { Header, Footer, Menu } from "../components/index";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);
    console.log("[App.js] Constructor");
    const token = localStorage.getItem("token");
    this.state = {
      isLogin: token !== null,
    };
    console.log("[App.js] token: ", token);
    console.log("[App.js] isLogin: ", this.state.isLogin);
    this.doLogin = this.doLogin.bind(this);
    this.doLogout = this.doLogout.bind(this);
  }

  doLogin() {
    console.log("[App.js] doLogin");
    this.setState({ isLogin: true }, () => {
      console.log("[App.js] isLogin after doLogin: ", this.state.isLogin);
    });
  }

  doLogout() {
    console.log("[App.js] doLogout");
    this.setState({ isLogin: false }, () => {
      console.log("[App.js] isLogin after doLogout: ", this.state.isLogin);
    });
  }

  render() {
    return (
      <div>
        <Header doLogout={this.doLogout} isLogin={this.state.isLogin} />
        <div className="centered">
          <Routes>
            <Route path="/" element={<Menu />} />
            <Route path="/like" element={<Menu />} />
            <Route path="/my" element={<Menu />} />
            <Route path="/main" element={<Main />} />
            <Route path="/like" element={<Like />} />
            <Route path="/my" element={<My />} />
          </Routes>
        </div>
        <div className="centered">
          <Routes>
            <Route path="/detail/:pk" element={<Detail />} />
            <Route
              path="/new"
              element={<New isLogin={this.state.isLogin} />}
            />
            <Route
              path="/profile"
              element={<Profile isLogin={this.state.isLogin} />}
            />
          </Routes>
        </div>
        <div>
          <Routes>
            <Route
              path="/login"
              element={<Login doLogin={this.doLogin} isLogin={this.state.isLogin} />}
            />
            <Route path="/register" element={<Register />} />
          </Routes>
        </div>
        <Footer />
      </div>
    );
  }
}

export default App;
