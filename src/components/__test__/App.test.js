import React from 'react';
import App from '../App';
import renderer from 'react-test-renderer';

describe('snapshot test', () => {
  it('render correctly', () => {
    const component = renderer.create(
      <App />
    );
    let tree = component.toJSON();
    expect(tree).toMatchSnapshot();
  })
});