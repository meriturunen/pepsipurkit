import React, { PureComponent } from 'react';
import { PieChart, Pie, Sector, Cell } from 'recharts';

const COLORS = ['#5fc82b','#8FD96B','#CFEFBF','#000a48','#4D547F','#B3B6C8','#0041db','#4D7AE6','#CCD9F8','#fe4545','#FE7D7D','#FFC7C7'];

const formatter = new Intl.NumberFormat('fi-FI', {
  style: 'currency',
  currency: 'EUR',
  minimumFractionDigits: 0
})

function toTitleCase(str) {
  return str.replace(
    /^[a-zA-Z]/g,
    function(txt) {
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    }
  ).replace('-', ' ').replace('-', ' ');
}

const renderActiveShape = (props) => {
    const RADIAN = Math.PI / 180;
    const {
        cx, cy, innerRadius, outerRadius, startAngle, endAngle,
        fill, payload
    } = props;
    var str = ''
    var result = str.concat(payload.name);
    var titleRes = toTitleCase(result);
    return (
        <g>
        <text x={cx} y={cy} dy={5} textAnchor="middle" fill={'#000000'}>{titleRes}</text>
        <text x={cx} y={cy} dy={30} textAnchor="middle" fill={'#000000'}>{payload.value} kpl</text>
        <Sector
            cx={cx}
            cy={cy}
            innerRadius={innerRadius}
            outerRadius={outerRadius + 8}
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
      <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} textAnchor={textAnchor} fill="#333">{toTitleCase(name)}</text>
    </g>
  );
};

export default class PikkudonitsiKpl extends PureComponent {
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

  onPieLeave = (data, index) => {
    this.setState({
      activeIndex: 999,
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
          onMouseEnter={this.onPieEnter}
          onMouseLeave={this.onPieLeave}
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
