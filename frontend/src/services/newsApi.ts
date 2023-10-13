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
      query: (query: string) => ({
        url: "/api/test",
        params: {
          _query: query
        }
      })
    }),
    postAllNews: builder.mutation<any[], any>({
      query: (request: ISearchRequest) => ({
        url: "/search/test",
        method: "POST",
        body: request
      })
    }),
  }),
});

export const { useGetAllNewsQuery, usePostAllNewsMutation } = newsApi;