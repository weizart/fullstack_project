import React, { useState,useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import positive_icon from "../assets/positive.png"
import neutral_icon from "../assets/neutral.png"
import negative_icon from "../assets/negative.png"
import review_icon from "../assets/reviewbutton.png"
import Header from '../Header/Header';

const Dealer = () => {
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [unreviewed, setUnreviewed] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [postReview, setPostReview] = useState(<></>);

  let curr_url = window.location.href;
  let root_url = curr_url.substring(0,curr_url.indexOf("dealer"));
  let params = useParams();
  let id = params.id;
  let dealer_url = root_url+`djangoapp/dealer/${id}`;
  let reviews_url = root_url+`djangoapp/reviews/dealer/${id}`;
  let post_review = root_url+`postreview/${id}`;
  
  const get_dealer = async () => {
    try {
      const res = await fetch(dealer_url);
      const retobj = await res.json();
      console.log("Dealer data:", retobj);
      
      if(retobj.status === 200 && retobj.dealer) {
        setDealer(retobj.dealer);
        console.log("Set dealer to:", retobj.dealer);
      } else {
        setError("Failed to load dealer data");
      }
    } catch (err) {
      console.error("Error in get_dealer:", err);
      setError("Error loading dealer data: " + err.message);
    }
  };

  const get_reviews = async () => {
    try {
      const res = await fetch(reviews_url);
      const retobj = await res.json();
      console.log("Reviews data:", retobj);
      
      if(retobj.status === 200) {
        if(retobj.reviews && retobj.reviews.length > 0) {
          setReviews(retobj.reviews);
          setUnreviewed(false);
        } else {
          setUnreviewed(true);
        }
      } else {
        setError("Failed to load reviews");
      }
    } catch (err) {
      console.error("Error in get_reviews:", err);
      setError("Error loading reviews: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const senti_icon = (sentiment) => {
    let icon = sentiment === "positive" ? positive_icon : 
               sentiment === "negative" ? negative_icon : 
               neutral_icon;
    return icon;
  };

  useEffect(() => {
    const loadData = async () => {
      if(sessionStorage.getItem("username")) {
        setPostReview(
          <a href={post_review}>
            <img 
              src={review_icon} 
              style={{width:'10%',marginLeft:'10px',marginTop:'10px'}} 
              alt='Post Review'
            />
          </a>
        );
      }
      await get_dealer();
      await get_reviews();
    };
    loadData();
  }, [dealer_url, reviews_url, post_review]);

  if (error) {
    return (
      <div style={{margin:"20px"}}>
        <Header/>
        <div className="error-message">{error}</div>
      </div>
    );
  }

  if (!dealer && loading) {
    return (
      <div style={{margin:"20px"}}>
        <Header/>
        <div>Loading dealer information...</div>
      </div>
    );
  }

  return (
    <div style={{margin:"20px"}}>
      <Header/>
      {dealer && (
        <div style={{marginTop:"10px"}}>
          <h1 style={{color:"grey"}}>
            {dealer.full_name}
            {sessionStorage.getItem("username") && postReview}
          </h1>
          <h4 style={{color:"grey"}}>
            {dealer.city}, {dealer.address}, Zip - {dealer.zip}, {dealer.state}
          </h4>
        </div>
      )}
      <div className="reviews_panel">
        {loading ? (
          <div>Loading Reviews....</div>
        ) : unreviewed ? (
          <div>No reviews yet!</div>
        ) : reviews.length > 0 ? (
          reviews.map((review, index) => (
            <div className='review_panel' key={index}>
              <img 
                src={senti_icon(review.sentiment)} 
                className="emotion_icon" 
                alt='Sentiment'
              />
              <div className='review'>{review.review}</div>
              <div className="reviewer">
                {review.name} {review.car_make} {review.car_model} {review.car_year}
              </div>
            </div>
          ))
        ) : (
          <div>No reviews available</div>
        )}
      </div>  
    </div>
  );
};

export default Dealer;
