import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';

import Layout from './Layout';
import Home from '../pages/Home';
import Login from '../pages/Login';
import Looking from '../pages/Looking';
import NotFound from '../pages/NotFound';

// apollo setup
const client = new ApolloClient({
  uri: 'https://angelmartinez04.pythonanywhere.com/api/graphql'
  // uri: 'http://localhost:8000/api/graphql'
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