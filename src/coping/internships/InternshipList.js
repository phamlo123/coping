/* eslint-disable */
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
        
        {internships.map((internship, index) =>
            <div key={index}>
            <li className="list-group-item">
                <div>{internship.owner}</div>
                <div>{internship.company}</div>
                <div>{internship.title}</div>
                <div>{internship.review}</div>
                <div>{internship.tasks}</div>
                <div>{internship.pay}</div>
            </li>
        </div>
        )}
        
        </ul>
    );
}

export default InternshipList;