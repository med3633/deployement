import {React, useEffect, useState} from "react";
import axios  from "axios";
import AdminLayout from "../hocs/AdminLayout";
import {Row, Col, Card} from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUsers, faUser, faBriefcase, faBuilding, faUsersCog, faCalendarDay } from '@fortawesome/free-solid-svg-icons';
import './Dashboard.css'
import ChartComponent from './ChartComponent';
import PieChart from './PieChart'


const Dashboard = (props) => {
    const [users, setUsers] = useState();
    const [usersThisMonth, setUserThisMonth] = useState(0)
    const [admins, setAdmins] = useState(0)
    const [condidats, setCondidats] = useState(0)
    const [employees, setEmployees] = useState(0)
    const [societes, setSocietes] = useState()
    const [genre, setGenre] = useState()
    const [userCounts, setUsersCounts] = useState();
    const [emploisCounts, setEmploisCounts] = useState();


    useEffect(() => {
        const fetchUsers = async () => {
        try {
            const response = await axios.get('/admin/users/');
            const emploisResponse = await axios.get('/get-emplois');
            setUsers(response.data);
            setEmploisCounts(emploisResponse.data)
        } catch (error) {
          //  console.error('Error fetching users:', error);
        }
        };
        fetchUsers();
    }, []);
    
    useEffect(()=>{
        if (users !== undefined){
            let adminCount = 0;
            let condidatCount =0;
            let employeesCount =0;
            let societesCount =0;
            let count = 0;
            for( let u in users.users){
                if (users.users[u].role === 'admin'){
                    adminCount++;
                }else if(users.users[u].role ==='candidat'){
                    condidatCount++;
                }else if(users.users[u].role ==='employeur'){
                    employeesCount++;
                }else{
                    societesCount++;
                }

                if(new Date(users.users[u].registration_date).getMonth() === new Date().getMonth()){
                    count++
                }
            }
            setAdmins(adminCount)
            setEmployees(employeesCount)
            setSocietes(societesCount)
            setCondidats(condidatCount)
            setUserThisMonth(count)
            let homme = 0
            let femme = 0
            let autres = 0
            for (let u in users.personnes){
                if ((users.personnes[u].genre).toLowerCase() === 'homme'){
                    homme ++;
                }else if ( (users.personnes[u].genre).toLowerCase() === 'femme'){
                    femme ++;
                }else{
                    autres ++;
                }
            }
            let userCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            let today = new Date()
            for (let u in users.users){
                let index = new Date(users.users[u].registration_date).getMonth()
                if(new Date(users.users[u].registration_date).getFullYear() === today.getFullYear())
                    userCounts[index] = userCounts[index]+1
            }

            let empCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for (let e in emploisCounts){
                let index = new Date(emploisCounts[e].date_postulation).getMonth()
                if(new Date(emploisCounts[e].date_postulation).getFullYear() === today.getFullYear())
                    empCounts[index] = empCounts[index]+1
            }
            setUsersCounts(userCounts)
            setEmploisCounts(empCounts)
            setGenre({'Homme': homme, 'Femme': femme, 'Autres': autres})
        }
    },[users])



    return (
        <>
           <AdminLayout>
                <Row className="justify-content-md-center mt-5">
                    <Col md={3}>
                        <Card className="cardDashboard">
                            <center><h3> <FontAwesomeIcon icon={faUsers} /> Utilisateurs</h3></center>
                            <hr className="custom-hr"></hr>
                            <h5> {users && users.users.length} </h5>
                        </Card>
                    </Col>
                    <Col md={3}>
                        <Card className="cardDashboard">
                            <center><h3> <FontAwesomeIcon icon={faUser} /> Les condidats</h3></center>
                            <hr className="custom-hr"></hr>
                            <h5> {condidats && condidats} </h5>
                        </Card>
                    </Col>
                    <Col md={3}>
                        <Card className="cardDashboard"> 
                            <center><h3> <FontAwesomeIcon icon={faBriefcase} /> Les employeurs</h3></center>
                            <hr className="custom-hr"></hr>
                            <h5> {employees && employees} </h5>
                        </Card>
                    </Col>
                    <Col md={3}>
                        <Card className="cardDashboard"> 
                            <center><h3> <FontAwesomeIcon icon={faBuilding} /> Les societes</h3></center>
                            <hr className="custom-hr"></hr>
                            <h5>{users && users.societes.length} </h5>
                        </Card>
                    </Col>
                </Row>
                <Row className="justify-content-md-center mt-5">
                    <Col md={6}>
                        <Card className="cardDashboard">
                            <center><h3> <FontAwesomeIcon icon={faUsersCog}  /> Admins</h3></center>
                            <hr className="custom-hr"></hr>
                            <h5> {admins && admins} </h5>
                        </Card>
                    </Col>
                    <Col md={6}>
                        <Card className="cardDashboard">
                            <center><h3> <FontAwesomeIcon icon={faCalendarDay} />Utilisateurs inscrit en ce mois</h3></center>
                            <hr className="custom-hr"></hr>
                            <h5> {usersThisMonth && usersThisMonth} </h5>
                        </Card>
                    </Col>
                </Row>
                <Row className="Charts">
                    <Col md={6}>
                        <center><h6 className="mt-5">Nombre d'utilisateurs inscrit par mois</h6></center>
                        { userCounts && <ChartComponent data={userCounts} label={'Utilisateurs'} />}
                    </Col>
                    <Col md={3}>
                        <center><h6 className="mt-5">Gender Distribution</h6></center>
                        {genre && <PieChart data={genre} name="gender" labels = {["Homme", "Femme", "Autres"]} colors = {['#2DAAE1', 'pink', 'black']} />}
                    </Col>
                    <Col md={3}>
                        <center><h6 className="mt-5">Employers Distribution</h6></center>
                        {(societes && employees) && <PieChart data={{'societes' : societes , 'employers': employees}} name="employers" labels = {["Sociétes", "Employeur"]} colors = {['#2DAAE1', 'pink']} />}
                    </Col>
                </Row>

                <Row className="Charts">
                    <Col md={12}>
                        <center><h6 className="mt-5">Nombre d'emplois publié par mois</h6></center>
                        { emploisCounts && <ChartComponent data={emploisCounts} label={'Emplois'} />}
                    </Col>
                </Row>
           </AdminLayout>
        </>
        );
  };
 export default Dashboard;