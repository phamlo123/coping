import React from "react";

function InternshipItem(internship) {
    // {
    //     internship = {
    //         "id": 1,
    //         "title": "title",
    //         "company": "smartleaf",
    //         "pay": 123,
    //         "review": "re"
    //     }
    // }
    console.log(internship)
    return(
        <li className="list-group-item">
            <div>{internship.company}</div>
            <div>{internship.title}</div>
            <div>{internship.review}</div>
            <div>{internship.pay}</div>
       </li>
    );
}

export default InternshipItem;