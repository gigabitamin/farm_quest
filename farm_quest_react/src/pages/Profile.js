import React, { useState, useEffect } from "react";
import axios from "axios";
import { Navigate } from 'react-router-dom';


const Profile = (props) => {
  const [isUpdate, setIsUpdate] = useState(false);
  const [nickname, setNickname] = useState("");
  const [position, setPosition] = useState("");
  const [subjects, setSubjects] = useState("");
  const [image, setImage] = useState("");
  const [newImage, setNewImage] = useState(null);

  useEffect(() => {
    getProfile();
  }, []);

  const fileChangeHandler = (event) => {
    event.preventDefault();
    const file = event.target.files[0];
    setNewImage(file);
    setImage(file["name"]);
  };

  const updateClick = (event) => {
    event.preventDefault();
    if (isUpdate === true) {
      updateProfile();
    } else {
      setIsUpdate((prevIsUpdate) => !prevIsUpdate);
    }
  };

  const handleChange = (event) => {
    const target = event.target;
    if (target.name === "nickname") setNickname(target.value);
    else if (target.name === "position") setPosition(target.value);
    else if (target.name === "subjects") setSubjects(target.value);
  };

  const updateProfile = () => {
    const token = localStorage.getItem("token");
    const formData = new FormData();
    formData.append("image", newImage);
    formData.append("nickname", nickname);
    formData.append("position", position);
    formData.append("subjects", subjects);

    axios
      .patch("http://localhost:8000/users/profile/", formData, {
        headers: {
          "content-type": "multipart/form-data",
          Authorization: `Token ${token}`,
        },
      })
      .then((response) => {
        if (response.status < 300) {
          props.navigate("/"); // navigate 추가
        }
      });
  };

  const getProfile = () => {
    const token = localStorage.getItem("token");
    axios
      .get("http://localhost:8000/users/profile/", {
        headers: {
          Authorization: `Token ${token}`,
        },
      })
      .then((response) => {
        if (response.status < 300) {
          setNickname(response.data["nickname"]);
          setPosition(response.data["position"]);
          setSubjects(response.data["subjects"]);
          setImage(response.data["image"]);
        }
      });
  };

  const renderContent = () => {
    const isLogin = props.isLogin;

    if (isLogin === false) {
      return <Navigate to="/login" />;
    }

    if (isUpdate === false) {
      return (
        <div className="container mcentered">
          <div className="profile-img">
            <div className="profile-img">
              <figure className="image is-128x128">
                <img
                  src={image}
                  onChange={handleChange}
                  alt="test"
                  width="256"
                />
              </figure>
            </div>
            <div className="texts mcentered">
              <h1 className="title" onChange={handleChange}>
                {nickname}
              </h1>
              <div className="tags are-medium">
                <span className="tag" onChange={handleChange}>
                  #{position}
                </span>
                {subjects.split(", ").map((subject, index) => {
                  return (
                    <span
                      className="tag"
                      onChange={handleChange}
                      key={index}
                    >
                      #{subject}
                    </span>
                  );
                })}
              </div>
              <div className="button is-primary" onClick={updateClick}>
                <span>프로필 수정하기</span>
              </div>
            </div>
          </div>
        </div>
      );
    } else {
      return (
        <div className="container mcentered">
          <div className="profile-img">
            <div className="profile-img">
              <div className="file has-name is-centered">
                <label className="file-label">
                  <input
                    className="file-input"
                    type="file"
                    name="image"
                    onChange={fileChangeHandler}
                  />
                  <span className="file-cta">
                    <span className="file-icon">
                      <i className="fas fa-upload"></i>
                    </span>
                    <span className="file-label">Choose a file…</span>
                  </span>
                  <span className="file-name">{image}</span>
                </label>
              </div>
            </div>
            <div className="texts mcentered">
              <input
                className="input is-primary is-medium"
                type="text"
                name="nickname"
                onChange={handleChange}
                placeholder={nickname}
              />
              <input
                className="input is-primary is-medium"
                type="text"
                name="position"
                onChange={handleChange}
                placeholder={position}
              />
              <input
                className="input is-primary is-medium"
                type="text"
                name="subjects"
                onChange={handleChange}
                placeholder={subjects}
              />
              <div className="button is-primary" onClick={updateClick}>
                <span>완료</span>
              </div>
            </div>
          </div>
        </div>
      );
    }
  };

  return renderContent();
};

export default Profile;