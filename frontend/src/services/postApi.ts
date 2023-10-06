import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { IPost } from "../models/IPost";

export const postApi = createApi({
  reducerPath: "postApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
  }),
  endpoints: (builder) => ({
    getAllPosts: builder.query<IPost[], number>({
      query: (limit: number) => ({
        url: "/api/test",
      })
    }),
  }),
});

export const { useGetAllPostsQuery } = postApi;