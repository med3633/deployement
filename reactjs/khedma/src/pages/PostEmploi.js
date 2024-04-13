import React , { useState, useEffect } from 'react'; 
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMapPin,faCircleXmark,faMessage,faComments,faHourglassStart
  ,faHourglassEnd,faStopwatch20,faVenusMars,faUser, faMoneyBill,
  faCalendarCheck} from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import { connect } from 'react-redux';
import IconButton from '@mui/material/IconButton';
import DeleteIcon from '@mui/icons-material/Delete';
import CryptoJS from 'crypto-js';
import { useNavigate} from 'react-router-dom';
import DOMPurify from 'dompurify';
import Modal from 'react-modal';

import './PostEmploi.css';

const PostEmploi = ({ titre, image_emploi, localisation, type_emploi, onclick, user, id ,description,
  date_postulation,
  date_expiration,
  duree_offre,
   genre_demande,
  intervalle_age,
   montant_paiement,
   experience}) => {
  
  const [modalIsOpen, setModalIsOpen] = useState(false);

  const navigate = useNavigate();
  const [employerName, setEmployerName] = useState('');
  const [idUser, setIdUser] = useState('');
  const [role, setRole] = useState('');
  const [prenom, setPrenom] = useState('');

  const createChat = async () => {
    try {
      const chatData = {
        members: [id, user]
      };
      
      const response = await axios.post('/CreateChat/', chatData);
  
      // If the request is successful, you can handle the response here.
      //console.log('Chat created:', response.data);
      // Navigate the user to the new chat page
      navigate('/chat');
      // Optionally, you can close the modal here if needed.
      closeModal();
    } catch (error) {
      navigate('/chat');
      // Handle any errors that occur during the request.
     // console.error('Error creating chat:', error);
    }
  };
  

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`/admin/users/${user}/`);
       // console.log("response test", response.data);
        setEmployerName(response.data.nom);
        setIdUser(response.data.id);
        setRole(response.data.role);
        if (response.data.role === "employeur") {
          setPrenom(response.data.prenom);
        }
      } catch (error) {
       // console.log(error);
      }
    }

    fetchData();
  }, [user]);

  const handleDetailEmployeurClick = () => {
    const encryptedId = CryptoJS.AES.encrypt(idUser.toString(), 'secretKey').toString();
    const encodedId = encodeURIComponent(encryptedId);
    if (role === "employeur") {
      navigate(`/detail-employeur/${encodedId}`);
    }
    if (role === "societe") {
      navigate(`/detail-societe/${encodedId}`);
    }
  };

  const openModal = () => {
    setModalIsOpen(true);
  };

  const closeModal = () => {
    setModalIsOpen(false);
  };

  return (
    <div className='body'>
      <section>
        <div className="postEmploi-container">
          <div className="postEmploi-content">
            <div className="postEmploi-card">
              <div className="postEmploi-card-content">
                <div className='postEmploi-image'>
                  <img src={image_emploi} alt="image" /><br />
                </div>
                <div className='postEmploi-titre'> 
                  <span className='titreEmploi'>{titre}</span>
                </div>
                <div className='postEmploi-nom-entreprise'>
                  <span className='nom-entreprise'> {employerName}&nbsp; {prenom}</span>
                </div> 
                <div className='postEmploi-titre'>
                  <button onClick={handleDetailEmployeurClick} className='titreEmploi' style={{ background: "white", borderColor: "white" }}>Publiée par: {employerName}&nbsp; {prenom}</button>
                </div>
                <div className='postEmploi-localisation'>
                  <div className="location-wrapper">
                    <span className='localisation'> {localisation}</span>
                  </div>
                </div>
                <div className="button-container">
                  <button className="button1" >{type_emploi}</button>
                  <button className="button2" onClick={openModal}>Postuler</button>
                </div> 
                {user === id && (
                  <DeleteIcon className='delete-icon' onClick={onclick} />
                )}
              </div>
            </div>
          </div>
        </div>
      </section>
     <Modal
  isOpen={modalIsOpen}
  onRequestClose={closeModal}
  contentLabel="Example Modal"
  className="custom-modal"
  overlayClassName="custom-overlay"
  id="jobModal"
  style={{
    content: {
      position: 'fixed',
      top: '50%',
      left: '50%',
      transform: 'translate(-50%, -50%)',
      width: '80%', // Initial width (adjust as needed)
      height: 'auto', // Initial height (adjust as needed)
      maxWidth: '50%', // Maximum width relative to the viewport width
      maxHeight: '90%', // Maximum height relative to the viewport height
    }
  }}
>

        <h4>Offre d'emploi : Lisez et postulez.</h4>
        <div className="scrollable-description">
        <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(description) }} />
         
          <p> Date de postulation: <br/><FontAwesomeIcon icon={faHourglassStart} className="blue-icon" /> {date_postulation}</p>
<p> Date d'expiration: <br/><FontAwesomeIcon icon={faHourglassEnd} className="blue-icon" /> {date_expiration}</p>
<p> Duree de l'offre: <br/><FontAwesomeIcon icon={faStopwatch20} className="blue-icon" /> {duree_offre}</p>
<p> Genre demandé: <br/><FontAwesomeIcon icon={faVenusMars} className="blue-icon" /> {genre_demande}</p>
<p> Intervalle d'age: <br/><FontAwesomeIcon icon={faUser} className="blue-icon" /> {intervalle_age}</p>
<p> Montant de paiement: <br/><FontAwesomeIcon icon={faMoneyBill} className="blue-icon" /> {montant_paiement}</p>
<p> Experience: <br/><FontAwesomeIcon icon={faCalendarCheck} className="blue-icon" /> {experience}</p>

        </div>
        
        <button className="button1" onClick={createChat}> <FontAwesomeIcon icon={faComments} /> Connecter </button>
        <br />
        <FontAwesomeIcon icon={faCircleXmark} onClick={closeModal} />

      </Modal>
    </div>
  );
};

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
  role: state.auth.user && state.auth.user.role,
  id: state.auth.user && state.auth.user.id,
});

const ConnectedPostEmploi = connect(mapStateToProps)(PostEmploi);

export default connect(mapStateToProps)(PostEmploi);