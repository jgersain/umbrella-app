// import axios from 'axios';
import React, { Component }  from 'react';
import { AUTH_TOKEN } from '../constants';
import { MDBContainer, MDBRow, MDBCol, MDBInput } from 'mdbreact';
import { Mutation } from 'react-apollo';
import { gql } from 'apollo-boost';

import './styles/Login.scss';

import Test from '../components/Test';

const SIGNUP_MUTATION = gql`
  mutation SignupMutation($email: String!, $password: String!, $username: String!) {
    createUser(email: $email, password: $password, username: $username) {
      token
    }
  }
`
const LOGIN_MUTATION = gql`
  mutation LoginMutation($username: String!, $password: String!) {
    tokenAuth(username: $username, password: $password) {
      token
    }
  }
`

class Login extends Component {
  state = {
    login: true,
    email: '',
    password: '',
    username: '',
    users: []
  }

  render() {  
    const { login, email, password, username } = this.state;
    return (
      <div id="login-wrapper">
        <MDBContainer id="login" className="card p-5 mt-5">
          <MDBRow>
            <MDBCol>
              <Test></Test>
              <div id="userForm">
                <p className="h4 text-center mb-4 font-weight-bold text-muted">
                  { login ? 'INICIAR SESIÓN' : 'REGISTRO'}
                </p>
                <div className="grey-text">
                  { !login && (
                    <MDBInput
                      label="Correo Electrónico"
                      value={ email }
                      onChange={e => this.setState({ email: e.target.value })}
                      icon="envelope"
                      group
                      type="email"
                      validate
                      required
                    />
                  )}
                  <MDBInput
                    label="Nombre de usuario"
                    value={ username }
                    onChange={e => this.setState({ username: e.target.value })}
                    icon="user"
                    group
                    type="text"
                    validate
                    required
                  />
                  <MDBInput
                    label="Constraseña"
                    value={ password }
                    onChange={e => this.setState({ password: e.target.value })}
                    icon="lock"
                    group
                    type="password"
                    validate
                    required
                  />
                </div>
                <div className="text-center">
                  <Mutation
                    mutation={login ? LOGIN_MUTATION : SIGNUP_MUTATION}
                    variables={{email, password, username}}
                    onCompleted={data => this._confirm(data)}
                  >
                    {
                      mutation => (
                        <button
                          onClick={mutation}
                          className="btn peach-gradient font-weight-bold"
                        > { login ? 'Iniciar Sesión' : 'Registrarse' }
                        </button>
                      )
                    }
                  </Mutation>
                </div>
              </div>
            </MDBCol>
            <MDBCol md='12' className="pt-4">
              <p className='font-small d-flex justify-content-end'>
                { login ? '¿No tienes una cuenta?' : '¿Ya tienes una cuenta?' }
                <span className='text-default ml-1 font-weight-bold'
                  onClick={() => this.setState({ login: !login })}
                >
                  { login ? 'Registrate aquí!' : 'Inicia sesión aquí!' }
                </span>
              </p>
            </MDBCol>
          </MDBRow>
        </MDBContainer>
      </div>  
    )
  }

  // implement the mutation that we need to send
  _confirm = async (data) => {
    const { token } = this.state.login ? data.tokenAuth : data.createUser
    
    this._saveUserData(token)
    this.props.history.push(`/looking`)

  }

  _saveUserData = token => {
    localStorage.setItem(AUTH_TOKEN, token);
  }
}

export default Login;