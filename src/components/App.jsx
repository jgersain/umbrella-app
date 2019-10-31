import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import ApolloClient from 'apollo-client';
import { ApolloProvider } from '@apollo/react-hooks';
import { setContext } from 'apollo-link-context';
import { createHttpLink } from 'apollo-link-http';
import { InMemoryCache } from 'apollo-cache-inmemory';

import Layout from './Layout';
import Home from '../pages/Home';
import Login from '../pages/Login';
import Looking from '../pages/Looking';
import NotFound from '../pages/NotFound';
import { AUTH_TOKEN } from '../constants';

// apollo setup
const httpLink = createHttpLink({
  uri: 'https://angelmartinez04.pythonanywhere.com/api/graphql',
  // uri: 'http://localhost:8000/api/graphql'
});

const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem(AUTH_TOKEN)
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : ''
    }
  }
})

const client = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache(),
});

const App = () => (
  <BrowserRouter>
    <ApolloProvider client={client}>
      <Layout>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/looking" component={Looking} />
          <Route component={NotFound} />
        </Switch>
      </Layout>
    </ApolloProvider>
  </BrowserRouter>
);

export default App;