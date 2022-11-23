import { configureStore }
  from '@reduxjs/toolkit';
import React from 'react';
import {Provider} from "react-redux";

import internshipsReducer from './reducers/internships-reducer';
import InternshipList from './internships/InternshipList';

const store = configureStore(
    {reducer: {
      internshipsData: internshipsReducer
    }});

function Coping() {
    return (
        <Provider store={store}>
            <InternshipList/>
        </Provider>
    );
}
       
export default Coping;