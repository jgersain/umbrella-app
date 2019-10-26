import React, { Component } from 'react';
import ReactDom from 'react-dom';
import MapStyles from './MapStyles'

const mapStyles = {
  map: {
    position: 'absolute',
    width: '100%',
    height: '100%'
  }
}

class MapLocation extends Component {
  constructor(props) {
    super(props);

    const { lat, lng } = this.props.initialCenter;
    this.state = {
      currentLocation: {
        lat: lat,
        lng: lng
      }
    }
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevProps.google !== this.props.google) {
      this.loadMap();
    }

    if (prevState.currentLocation !== this.state.currentLocation) {
      this.recenterMap();
    }
  }

  componentDidMount() {
    if (this.props.centerAroundCurrentLocation) {
      if (navigator && navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(pos => {
          const { latitude, longitude } = pos.coords;
          console.log(`Lat: ${latitude} Lng: ${longitude}`)
          this.setState({
            currentLocation: {
              lat: latitude,
              lng: longitude
            }
          })
        })
      }
    }
    this.loadMap();
  }

  loadMap() {
    if (this.props && this.props.google) {
      const { google } = this.props;
      const maps = google.maps;

      const mapRef = this.refs.map;

      const node = ReactDom.findDOMNode(mapRef);

      let { zoom } = this.props;
      const { lat, lng } = this.state.currentLocation;
      const center = new maps.LatLng(lat, lng);
      const mapConfig = Object.assign(
        {},
        {
          center: center,
          zoom: zoom, 
          styles: MapStyles
        }
      );

      this.map = new maps.Map(node, mapConfig);
    }
  }

  recenterMap() {
    const map = this.map;
    const current = this.state.currentLocation;

    const google = this.props.google;
    const maps = google.maps;

    if (map) {
      let center = new maps.LatLng(current.lat, current.lng);
      map.panTo(center);
    }
  }

  renderChildren() {
    const { children } = this.props;
    if (!children) return;
  
    return React.Children.map(children, c => {
      if (!c) return;
      return React.cloneElement(c, {
        map: this.map,
        google: this.props.google,
        mapCenter: this.state.currentLocation
      })
    })
  }

  render() {
    const style = Object.assign({}, mapStyles.map);
    
    return (
      <div>
        <div style={style} ref="map">
          Loading map...
        </div>
        { this.renderChildren() }
      </div>
    )
  }
}

MapLocation.defaultProps = {
  zoom: 16,
  initialCenter: { 
    lat: 19.4359883, 
    lng: -99.1549316 
  }, 
  centerAroundCurrentLocation: false,
  visible: true
};

export default MapLocation;

