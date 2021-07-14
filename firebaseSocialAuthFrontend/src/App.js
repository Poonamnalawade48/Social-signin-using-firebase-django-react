import * as React from "react";
import { render } from "react-dom";
import axios from "axios";
import firebase from "firebase/app";
import "firebase/auth";
import {
  FirebaseAuthProvider,
  FirebaseAuthConsumer,
  IfFirebaseAuthed,
  IfFirebaseAuthedAnd,
} from "@react-firebase/auth";
import { firebaseConfig } from "./config";
import { toast } from "react-toastify";

console.log(firebaseConfig);
firebase.initializeApp(firebaseConfig);
function App() {
  const [res, setRes] = React.useState(null);
  return (
    <FirebaseAuthProvider {...firebaseConfig} firebase={firebase}>
      <div>
        <button
          onClick={() => {
            const googleAuthProvider = new firebase.auth.GoogleAuthProvider();
            firebase
              .auth()
              .signInWithPopup(googleAuthProvider)
              .then((result) => {
                console.log(result);
              })
              .catch((error) => {
                // Handle Errors here.
                var errorCode = error.code;
                var errorMessage = error.message;
                // The email of the user's account used.
                var email = error.email;
                // The firebase.auth.AuthCredential type that was used.
                var credential = error.credential;
                // ...
                toast.error(error.message, {
                  position: toast.POSITION.BOTTOM_RIGHT,
                });
              });
          }}
        >
          Sign In with Google
        </button>
        <button
          onClick={() => {
            const facebookAuthProvider =
              new firebase.auth.FacebookAuthProvider();
            firebase
              .auth()
              .signInWithPopup(facebookAuthProvider)
              .then((result) => {
                console.log(result);
              })
              .catch((error) => {
                // Handle Errors here.
                var errorCode = error.code;
                var errorMessage = error.message;
                // The email of the user's account used.
                var email = error.email;
                // The firebase.auth.AuthCredential type that was used.
                var credential = error.credential;
                // ...
                toast.error(error.message, {
                  position: toast.POSITION.BOTTOM_RIGHT,
                });
              });
          }}
        >
          Sign In with Facebook
        </button>
        <button
          onClick={() => {
            const githubAuthProvider = new firebase.auth.GithubAuthProvider();
            firebase
              .auth()
              .signInWithPopup(githubAuthProvider)
              .then((result) => {
                console.log(result);
              })
              .catch((error) => {
                // Handle Errors here.
                var errorCode = error.code;
                var errorMessage = error.message;
                // The email of the user's account used.
                var email = error.email;
                // The firebase.auth.AuthCredential type that was used.
                var credential = error.credential;
                // ...
                toast.error(error.message, {
                  position: toast.POSITION.BOTTOM_RIGHT,
                });
              });
          }}
        >
          Sign In with Github
        </button>
        <button
          onClick={() => {
            firebase.auth().signOut();
          }}
        >
          Sign Out
        </button>
        <FirebaseAuthConsumer>
          {({ isSignedIn, user, providerId }) => {
            if (isSignedIn) {
              firebase
                .auth()
                .currentUser.getIdToken(/* forceRefresh */ true)
                .then(function (idToken) {
                  // Send token to your backend via HTTPS
                  // ...
                  console.log(idToken);
                  let config = {
                    headers: {
                      Authorization: "Bearer " + idToken,
                    },
                  };

                  axios
                    .post(
                      `http://127.0.0.1:8000/api/authentication/socialSignup`,
                      null,
                      config
                    )
                    .then((res) => {
                      console.log(res);
                      console.log(res.data);
                      toast.success(res.data.message, {
                        position: toast.POSITION.BOTTOM_RIGHT,
                      });
                    });
                })
                .catch(function (error) {
                  // Handle error
                  console.log(error);
                  toast.error(error.message, {
                    position: toast.POSITION.BOTTOM_RIGHT,
                  });
                });
            }
            return (
              <pre style={{ height: 300, overflow: "auto" }}>
                {JSON.stringify({ isSignedIn, user, providerId }, null, 2)}
              </pre>
            );
          }}
        </FirebaseAuthConsumer>
        <div>
          <IfFirebaseAuthed>
            {() => {
              return <div>You are authenticated</div>;
            }}
          </IfFirebaseAuthed>
          <IfFirebaseAuthedAnd
            filter={({ providerId }) => providerId !== "anonymous"}
          >
            {({ providerId }) => {
              return <div>You are authenticated with {providerId}</div>;
            }}
          </IfFirebaseAuthedAnd>
        </div>
      </div>
    </FirebaseAuthProvider>
  );
}

export default App;
