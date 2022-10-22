import React from "react";

function InternshipItem(internship_item) {

    return(
        <li className="list-group-item">
            <div>{internship_item.company}</div>
            <div>{internship_item.title}</div>
            <div>{internship_item.review}</div>
            <div>{internship_item.pay}</div>
       </li>
    );
}

export default InternshipItem;