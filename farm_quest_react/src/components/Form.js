import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const Form = () => {
  const history = useNavigate();

  const [state, setState] = useState({
    title: "",
    category: "",
    body: "",
    image: null,
    imageName: "",
  });

  const handleChange = (event) => {
    const target = event.target;
    setState((prevState) => ({ ...prevState, [target.name]: target.value }));
  };

  const fileChangeHandler = (event) => {
    event.preventDefault();
    const file = event.target.files[0];
    setState((prevState) => ({ ...prevState, image: file, imageName: file["name"] }));
  };

  const postClick = () => {
    const token = localStorage.getItem("token");
    console.log("[*] createPost");

    const formData = new FormData();
    formData.append("Title", state.title);
    formData.append("Content", state.body);

    axios
      .post("http://127.0.0.1:8000/posts/", formData, {
        headers: {
          "content-type": "multipart/form-data",
          Authorization: `Token ${token}`,
        },
      })
      .then((response) => {
        if (response.status < 300) {
          history.push("/");
        }
      });
  };


    return (
      <div>
        <div className="field">
          <label className="label">제목</label>
          <div className="control">
            <input
              className="input is-hovered"
              type="text"
              name="title"
              onChange={handleChange}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">카테고리</label>
          <div className="control">
            <div className="select">
              <select>
                <option>공지사항</option>
                <option>FAQ</option>
                <option>풀로그</option>
                <option>질문/답변</option>
                <option>가드닝 샵</option>
              </select>
            </div>
          </div>
        </div>

        <div className="field">
          <label className="label">본문</label>
          <div className="control">
            <textarea
              className="textarea is-hovered"
              rows="10"
              name="body"
              onChange={handleChange}
            ></textarea>
          </div>
        </div>

        <div className="field">
          <label className="label">이미지</label>
          <div className="control">
            <div className="file has-name">
              <label className="file-label">
                <input
                  className="file-input"
                  type="file"
                  name="image"
                  onChange={fileChangeHandler}
                />
                <span className="file-cta">
                  <span className="file-label">Choose a file…</span>
                </span>
                <span className="file-name">{state.imageName}</span>
              </label>
            </div>
          </div>
        </div>
        <div className="field is-grouped">
          <div className="control">
            <button className="button is-primary" onClick={postClick}>
              완료
            </button>
          </div>
        </div>
      </div>
    );
  }


export default Form;
