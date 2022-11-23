import {createAsyncThunk}
  from "@reduxjs/toolkit"
import * as service
  from "./internships-service"

  export const findInternshipsThunk = createAsyncThunk(
      'tuits/findTuits', async () =>
          await service.findInternships()
  )
  
  export const deleteInternshipThunk = createAsyncThunk(
      'tuits/deleteTuit',
      async (internshipId) => {
          await service.deleteInternship(internshipId);
          return internshipId;
      }
  )
  
  export const createInternshipThunk = createAsyncThunk(
      'tuits/createTuit',
      async (internship) =>
          await service.createInternship(internship)
  )
  
  export const updateInternshipThunk = createAsyncThunk(
      'tuits/updateTuit',
      async (internship) =>
          await service.updateInternship(internship)
  )
  