import React from 'react';
import { MDBBtn, MDBCard, MDBCardBody, MDBCardImage, MDBCardTitle, MDBCardText, MDBCol } from 'mdbreact';
import { useQuery } from '@apollo/react-hooks';
import { gql } from 'apollo-boost';

const PROFILE_QUERY = gql`
  query {
    me {
      id
      username
    }
  }
`;

const Card = props => {
  // const { loading, error, data } = useQuery(PROFILE_QUERY);
  const { data } = useQuery(PROFILE_QUERY);
  console.log(data);
  
  // if (loading) {
  //   return <p className="navbar-text navbar-right">Loading...</p>;
  // }
  return (
    <MDBCol>
      { props.visible &&
        <MDBCard color="rainy-ashville-gradient" style={{ width: "20rem"}}>
          <MDBCardImage className="img-fluid" waves />
          <MDBCardBody>
            <MDBCardTitle className="font-weight-bold text-white">
              Paraguas {props.current} activado</MDBCardTitle>
            <MDBCardText>
              Aquí datos relevantes...
            </MDBCardText>
            <MDBBtn 
              gradient="purple"
              onClick={props.onClose}
            >Terminar</MDBBtn>
          </MDBCardBody>
        </MDBCard>
      }
    </MDBCol>
  )
}

export default Card;

