import {createSlice}
  from "@reduxjs/toolkit";
// import tuits from '../tuits/tuits.json';
import {findInternshipsThunk, deleteInternshipThunk, createInternshipThunk, updateInternshipThunk} from "../services/internships-thunk"

const initialState = {
   internships: [],
   loading: false
}

const tuitsSlice = createSlice({
 name: 'internships',
 initialState,
 extraReducers: {
  [findInternshipsThunk.pending]:
    (state) => {
        state.loading = true
        state.internships = []
  },
  [findInternshipsThunk.fulfilled]:
  (state, { payload }) => {
  state.loading = false
  state.internships = payload
  },
  [findInternshipsThunk.rejected]:
  (state) => {
      state.loading = false
  },
  [deleteInternshipThunk.fulfilled] :
  (state, { payload }) => {
  state.loading = false
  state.internships = state.internships
    .filter(t => t.id !== payload)
  },

  [createInternshipThunk.fulfilled]:
  (state, { payload }) => {
    state.loading = false
    state.internships.push(payload)
  },

  [updateInternshipThunk.fulfilled]:
  (state, { payload }) => {
    state.loading = false
    const internshipNdx = state.internships
      .findIndex((internship) => internship.id === payload.id)
    state.internships[internshipNdx] = {
      ...state.internships[internshipNdx],
      ...payload
    }
  },

},
reducers: { 
  // ...
}
});

export default tuitsSlice.reducer;   
