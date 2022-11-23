import React from "react";
// import RetrieveInternships from "./get"
const BASE_URL = "https://coping-backend.herokuapp.com/"


// let internships = RetrieveInternships("http://localhost:8000/internships/");

import InternshipList from "./InternshipList";
const Internships = async () => {
    return (
        <div>
            <InternshipList/>
        </div>
    );
}

export default Internships;