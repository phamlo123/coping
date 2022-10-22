import React from "react";
import './App.css';
import Login from "./coping/login";
import {BrowserRouter} from "react-router-dom";
import {Routes, Route} from "react-router";
import Signup from "./coping/signup";
import Internships from "./coping/internships";

import axios from 'axios';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'


function App() {
  return (
    <BrowserRouter>

    <div className="Container">
      <Routes>
        <Route index element={<Internships/>}/>
        <Route path="/login"
                  element={<Login/>}/>
        <Route path="/signup"
                  element={<Signup/>}/>
      </Routes>

    </div>
    </BrowserRouter>
  );
}

export default App;
