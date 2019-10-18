import React from "react";
import { Link } from 'react-router-dom'
import { MDBContainer, MDBRow, MDBCol, MDBInput, MDBBtn, MDBCard, MDBCardBody } from 'mdbreact';

const Login = () => {
  return (
    <div className="d-flex align-items-center justify-content-center mt-5">
      <MDBContainer className="col-md-6">
        <MDBRow>
          <MDBCol>
            <MDBCard>
              <MDBCardBody className="px-5">
                <form>
                  <p className="h4 text-center py-4 text-muted">REGISTRO</p>
                  <div className="grey-text">
                    <MDBInput
                      label="Nombre de usuario"
                      icon="user"
                      group
                      type="text"
                      validate
                      error="wrong"
                      success="right"
                    />
                    <MDBInput
                      label="Correo electrónico"
                      icon="envelope"
                      group
                      type="email"
                      validate
                      error="wrong"
                      success="right"
                    />
                    <MDBInput
                      label="Contraseña"
                      icon="lock"
                      group
                      type="password"
                      validate
                    />
                    <MDBInput
                      label="Confirma tu contraseña"
                      group
                      icon="lock"
                      type="password"
                      validate
                    />
                  </div>
                  <div className="text-center mt-2">
                    <MDBBtn className="btn peach-gradient font-weight-bold" type="submit">
                      Register
                    </MDBBtn>
                  </div>
                  <MDBCol md='12' className="mt-3">
                    <p className='font-small d-flex justify-content-end'>
                      ¿Ya tienes una cuenta?
                      <Link to='/login' className='text-default ml-1 font-weight-bold'>
                        Inicia sesión aquí! 
                      </Link>
                    </p>
                  </MDBCol>
                </form>
              </MDBCardBody>
            </MDBCard>
          </MDBCol>
        </MDBRow>
      </MDBContainer>
    </div>
  );
};

export default Login;