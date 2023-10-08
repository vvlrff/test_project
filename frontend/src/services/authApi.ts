import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const authApi = createApi({
  reducerPath: "authApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://localhost:8080",
  }),
  endpoints: (builder) => ({
    loginUser: builder.mutation({
      query: (body: { email: string, password: string }) => {
        return {
          url: "/api/auth/login",
          method: "post",
          body,
        }
      }
    }),
    registerUser: builder.mutation({
      query: (body: { 
        fullname: string, 
        username: string, 
        email: string, 
        password: string, 
        confirmPassword: string 
      }) => {
        return {
          url: "/api/auth/register",
          method: "post",
          body,
        }
      }
    }),
  }),
});

export const { useLoginUserMutation, useRegisterUserMutation } = authApi;