import { PieChart, Pie, Cell, Tooltip } from "recharts";

const data = [
  { name: "High", value: 5 },
  { name: "Medium", value: 12 },
  { name: "Low", value: 10 },
];

const COLORS = ["#ef4444", "#f59e0b", "#10b981"];

function AlertChart() {

  return (
    <div style={{
      background:"#1e293b",
      padding:"20px",
      borderRadius:"10px",
      marginTop:"20px"
    }}>

      <h2 style={{color:"white"}}>Alert Distribution</h2>

      <PieChart width={400} height={250}>
        <Pie
          data={data}
          dataKey="value"
          cx="50%"
          cy="50%"
          outerRadius={80}
          label
        >
          {data.map((entry, index) => (
            <Cell key={index} fill={COLORS[index]} />
          ))}
        </Pie>

        <Tooltip />
      </PieChart>

    </div>
  );
}

export default AlertChart;