import React, { PureComponent } from 'react';
import { PieChart, Pie, Sector, Cell } from 'recharts';

const COLORS = ['#5fc82b','#8FD96B','#CFEFBF','#000a48','#4D547F','#B3B6C8','#0041db','#4D7AE6','#CCD9F8','#fe4545','#FE7D7D','#FFC7C7'];

const formatter = new Intl.NumberFormat('fi-FI', {
  style: 'currency',
  currency: 'EUR',
  minimumFractionDigits: 0
})

const renderActiveShape = (props) => {
    const RADIAN = Math.PI / 180;
    const {
        cx, cy, innerRadius, outerRadius, startAngle, endAngle,
        fill, payload, isCurrency, isValueMark, valueMark
    } = props;
    var bigValue = 'ASDASDA';
    if (isCurrency === 'true') {
        bigValue = formatter.format(payload.value).toString;
    } else if (isValueMark === 'true') {
        bigValue = bigValue.concat(payload.value, ' ', valueMark);
    } else {
        bigValue = payload.value.toString;
    }
    return (
        <g>
        <text x={cx} y={cy} dy={5} textAnchor="middle" fill={'#000000'}>{payload.name}</text>
        <text x={cx} y={cy} dy={30} textAnchor="middle" fill={'#000000'}>{bigValue}</text>
        <Sector
            cx={cx}
            cy={cy}
            innerRadius={innerRadius}
            outerRadius={outerRadius}
            startAngle={startAngle}
            endAngle={endAngle}
            fill={fill}
        />
        </g>
    );
};


const renderCustomizedLabel = (
  { cx, cy, midAngle, innerRadius, outerRadius, index, fill, name }
  ) => {
  const RADIAN = Math.PI / 180;
  const sin = Math.sin(-RADIAN * midAngle);
  const cos = Math.cos(-RADIAN * midAngle);
  const sx = cx + (outerRadius + 10) * cos;
  const sy = cy + (outerRadius + 10) * sin;
  const mx = cx + (outerRadius + 30) * cos;
  const my = cy + (outerRadius + 30) * sin;
  const ex = mx + (cos >= 0 ? 1 : -1) * 22;
  const ey = my;
  const textAnchor = cos >= 0 ? 'start' : 'end';
  return (
    <g>
      <path d={`M${sx},${sy}L${mx},${my}L${ex},${ey}`} stroke={'#000000'} fill="none" />
      <circle cx={ex} cy={ey} r={2} fill={'#000000'} stroke="none" />
      <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} textAnchor={textAnchor} fill="#333">{name}</text>
    </g>
  );
};

export default class Pikkudonitsi extends PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      isFetching: false,
      data: []
    };
  }
  state = {
    activeIndex: 0,
  };

  onPieEnter = (data, index) => {
    this.setState({
      activeIndex: index,
    });
  };  

  render() {

    return (
      <>
      {!this.state.isFetching &&(
      <PieChart width={600} height={350}>
        <Pie
          activeIndex={this.state.activeIndex}
          activeShape={renderActiveShape}
          data={this.state.data}
          cx={300}
          cy={150}
          innerRadius={100}
          outerRadius={110}
          dataKey="value"
          onClick={this.onPieEnter}
          label={renderCustomizedLabel}
        >
          {
            this.state.data.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)
          }
        </Pie>
      </PieChart>)}
      </>
    );
  }

  componentDidMount(){
    this.setState({...this.state,isFetching:true})
		fetch(this.props.url)
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
