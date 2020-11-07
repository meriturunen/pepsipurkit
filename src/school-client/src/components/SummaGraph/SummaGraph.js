import React, { Component, PureComponent } from 'react';
import {
  BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend,Scatter
} from 'recharts';

export default class Example extends Component 
{
  constructor(props) {
    super(props);
    this.state = {
      isFetching: false,
      data: []
    };
  }
  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/30763kr7/';
  render() {
    return (
      <>
      {!this.state.isFetching &&(
      <BarChart
        width={500}
        height={300}
        data={this.state.data}
        margin={{
          top: 5, right: 30, left: 20, bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <YAxis/>
        {//<XAxis dataKey="SummienTodennakoisyys"/>
        }
        <Tooltip />
        <Legend />
        <Bar dataKey="sum" fill="#8884d8" />
        <Bar dataKey="tulot" fill="#82ca9d" />
        {//<Bar dataKey="unique" fill="#82ca9d" />
        }
      </BarChart>)}
      </>
    );
  }
  componentDidMount(){
    this.setState({...this.state,isFetching:true})
		fetch("http://localhost:5000/api/v1/summat/hist")
		.then((response)=>{
			return response.json();
		})
		.then((data)=> {
      console.log(data)
      this.setState({data:data,isFetching:false})
			}
		);
	}
}
