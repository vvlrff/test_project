import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { INews } from "../models/INews";
import { ISearchRequest } from "../models/ISearchRequest";

export const newsApi = createApi({
  reducerPath: "newsApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
    prepareHeaders: (headers, { getState }) => {
      const token = JSON.parse(localStorage.getItem('user') || '{}')?.access_token;
      if (token) {
        headers.set('Authorization', `Bearer ${token}`);
      }
      return headers;
    },
  }),
  endpoints: (builder) => ({
    getAllNews: builder.query<INews[], any>({
      query: () => ({
        url: "/api/test",
      })
    }),
    getNews: builder.query<INews, {id: number}>({
      query: (id) => ({
        url: `/api/test${id}`,
      })
    }),
    postAllNews: builder.mutation<INews[], ISearchRequest>({
      query: (request) => ({
        url: "/search/test_message_date",
        method: "POST",
        body: request
      })
    }),
    postAllNewsMessage: builder.mutation<INews[], {message: string}>({
      query: (request) => ({
        url: "/search/test_message",
        method: "POST",
        body: request
      })
    }),
  }),
});

export const { useGetAllNewsQuery, useGetNewsQuery, usePostAllNewsMessageMutation, usePostAllNewsMutation } = newsApi;