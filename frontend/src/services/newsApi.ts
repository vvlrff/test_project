import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { INews } from "../models/INews";

export const newsApi = createApi({
  reducerPath: "newsApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
  }),
  endpoints: (builder) => ({
    getAllNews: builder.query<INews[], string>({
      query: (query: string) => ({
        url: "/api/test",
        params: {
          _query: query
        }
      })
    }),
  }),
});

export const { useGetAllNewsQuery } = newsApi;