import React from 'react';
import axios from "axios";

class InternshipList extends React.Component {
    state = {
        internships: [],
    };

    async componentDidMount() {
        let data;

        let response = await axios.get("http://localhost:8000/internships/");
        data = response.data;
        this.setState({
            internships: data,
        }); 
    }

    render() {
        return(
            <ul className="list-group">
                {this.state.internships.map((internship, id) =>
                <div key={id}>
                <li className="list-group-item">
                    <div>{internship.company}</div>
                    <div>{internship.title}</div>
                    <div>{internship.review}</div>
                    <div>{internship.pay}</div>
                </li>
                </div>
                )}
            </ul>);
    }
}
export default InternshipList;