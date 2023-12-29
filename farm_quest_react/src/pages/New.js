import React from "react";
// import { Navigate, useNavigate } from "react-router-dom";
import { Navigate } from "react-router-dom";
import { Form } from "../components/index";

const New = (props) => {
  // const navigate = useNavigate();
  const isLogin = props.isLogin;

  // const handleButtonClick = () => {
  //   // 버튼 클릭 시 다른 경로로 이동
  //   navigate("/");
  // };

  if (isLogin === false) {
    return <Navigate to="/login" />;
  }

  return (
    <div className="container is-half">
      <Form />
      {/* <button onClick={handleButtonClick}>이동</button> */}
      <br />
    </div>
  );
};

export default New;
