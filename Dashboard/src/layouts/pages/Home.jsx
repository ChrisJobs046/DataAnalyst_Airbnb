import { useNavigate } from "react-router-dom";
import Grid from "@mui/material/Grid";
import Paper from "@mui/material/Paper";
import services from "../utils/services";
import useStyles from "../styles/home";

export function Home(props) {
const classes = useStyles();
const navigate = useNavigate();
return (
<>
    <h6 className={classes.hello}>Hola, Bienvenido!</h6>

    <Grid container spacing={2} {...props}>
    {services.map(({ name, href, Icon }, i) => (
        <Grid item xs={12} sm={6} md={6} lg={3} key={name}>
        <Paper className={classes.serviceCard} onClick={() => navigate(href || "/")}>
            <div className={classes.serviceCardIcon}>
            <Icon />
            </div>
            <h6 className={classes.serviceCardText}>{name}</h6>
        </Paper>
        </Grid>
    ))}
    </Grid>
</>
);
}

export default Home;