import axios from 'axios';
import React, { Component }  from 'react';
import { AUTH_TOKEN } from '../constants';
import { MDBContainer, MDBRow, MDBCol, MDBInput } from 'mdbreact';

import './styles/Login.scss';

class Login extends Component {
  state = {
    login: true,
    email: '',
    password: '',
    username: '',
    users: []
  }

  async validate() {
    // let response = await axios({
    //   url: 'http://localhost:8000/api/graphql',
    //   method: 'POST',
    //   data: {
    //     query: `
    //       mutation CreateUser {
    //         CrearUsuario
    //         (
    //           nombre: "Ezio Auditore",
    //           email: "ezio@auditore.com",
    //           clave: "startx"
    //           confirmarClave: "startx"
    //         ){
    //           respuesta
    //           mensaje
    //         }
    //       }
    //     `
    //   }
    // }).then((result) => {
    //   console.log(result.data)
    // });
    // console.log(response);
    
    // this.setState({ users: response.data })
  }

  render() {
    const { login, email, password, username } = this.state;
    return (
      <div id="login-wrapper">
        <MDBContainer id="login" className="card p-5 mt-5">
          <MDBRow>
            <MDBCol>
              <form>
                <p className="h4 text-center mb-4 font-weight-bold text-muted">
                  { login ? 'INICIAR SESIÓN' : 'REGISTRO'}
                </p>
                <div className="grey-text">
                  { !login && (
                    <MDBInput
                      label="Nombre de usuario"
                      value={ username }
                      onChange={e => this.setState({ name: e.target.value })}
                      icon="user"
                      group
                      type="text"
                      validate
                      error="wrong"
                      success="right"
                    />
                  )}
                  <MDBInput
                    name="email"
                    value={ email }
                    label="Correo Electrónico"
                    icon="envelope"
                    group
                    type="email"
                    validate
                    error="wrong"
                    success="right"
                    onChange={e => this.setState({ email: e.target.value })}
                  />
                  <MDBInput
                    name="password"
                    value={ password }
                    onChange={e => this.setState({ password: e.target.value })}
                    label="Constraseña"
                    icon="lock"
                    group
                    type="password"
                    validate
                  />
                </div>
                <div className="text-center">
                  <button 
                    onClick={() => this._confirm()}
                    className="btn peach-gradient font-weight-bold"
                  > { login ? 'Iniciar Sesión' : 'Registrarse' }
                  </button>
                </div>
              </form>
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
  _confirm = async () => {
    // TODO implement this
    this.validate();
    this.props.history.push(`/looking`)
  }

  _saveUserData = token => {
    localStorage.setItem(AUTH_TOKEN, token);
  }
}

export default Login;