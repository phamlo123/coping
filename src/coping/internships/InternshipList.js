import React, {useEffect} from 'react';
import {useDispatch, useSelector} from "react-redux";
import { findInternshipsThunk } from '../services/internships-thunk';
import InternshipItem from './InternshipItem';


const InternshipList = () => {
    const dispatch = useDispatch();
    const {internships, loading} = useSelector(state => state.internshipsData)
 

    useEffect(() => {
      dispatch(findInternshipsThunk())
    }, [])
    
    return(
        <ul className="list-group">
        {
        loading &&
        <li className="list-group-item">
        Loading...
        </li>
        }
    
        {
            internships.map((internship, index) => <InternshipItem key={Math.random()} internship={internship}/>)
        }
        </ul>
    );
}

export default InternshipList;