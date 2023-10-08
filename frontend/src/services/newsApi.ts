import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { INews } from "../models/INews";
import { ISearchRequest } from "../models/ISearchRequest";

export const newsApi = createApi({
  reducerPath: "newsApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
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
        url: "/api/test_time",
        method: "POST",
        body: request
      })
    }),
  }),
});

export const { useGetAllNewsQuery, usePostAllNewsMutation } = newsApi;