import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const botApi = createApi({
  reducerPath: "botApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
    prepareHeaders: (headers, { getState }) => {
      const token = JSON.parse(localStorage.getItem('user') || '{}')?.access_token;
      if (token) {
        headers.set('Authorization', `Bearer ${token}`);
      }
      headers.set('Content-Type', 'application/json');
      return headers;
    },
  }),
  endpoints: (builder) => ({
    sendToGptMessage: builder.mutation<string, { message: string }>({
      query: (request) => ({
        url: "/bot/send_bot",
        method: "POST",
        body: request
      })
    }),
  }),
});

export const { useSendToGptMessageMutation } = botApi;