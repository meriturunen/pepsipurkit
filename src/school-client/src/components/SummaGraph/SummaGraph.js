import React, { PureComponent } from 'react';
import {
  BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend,
} from 'recharts';

var _data;
export default class Example extends PureComponent {
  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/30763kr7/';
  render() {
    return (
      <>
      {_data &&(
      <BarChart
        width={500}
        height={300}
        data={_data}
        margin={{
          top: 5, right: 30, left: 20, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="SummienTodennakoisyys" fill="#8884d8" />
        <Bar dataKey="unique" fill="#82ca9d" />
      </BarChart>)}
      </>
    );
  }
  componentDidMount(){
		fetch("http://localhost:5000/api/v1/summat")
		.then(function(response) {
			return response.json();
		})
		.then(function(data) {
      _data=data;
      console.log(_data)
			}
		);
	}
}
