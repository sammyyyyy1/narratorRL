import React, { useState, useEffect } from "react";
import { StyleSheet, ImageBackground, View, TouchableOpacity, Text, Pressable } from "react-native";
import { Ionicons, AntDesign } from "@expo/vector-icons";
import * as Speech from 'expo-speech';


export default function Capture({ navigation, route }) {
  const glasses = 'Glasses are really versatile. First, you can have glasses-wearing girls take them off and suddenly become beautiful, or have girls wearing glasses flashing those cute grins!';
  const [progress, setProgress] = useState(false);
  const [paused, setPaused] = useState(false);
  const { uri } = route.params;

  const speak = (text) => {
    //const glasses = 'Hello world!';
    const start = () => {
      setProgress(true);
    };
    
    const finish = () => {
      setProgress(false);
      setPaused(false);
      //setText("");
    }

    const options = {
      pitch: 1.0,
      rate: 1.05,
      onStart: start,
      onDone: finish,
      onStopped: finish,
      onError: finish
    };
    console.log(text);
    Speech.speak(text, options);
  };

  const pause = async () => {
    await Speech.pause();
    setPaused(true);
    console.log('pause');
  }

  const resume = () => {
    Speech.resume();
    setPaused(false);
    console.log('resume');
  }

  const stop = () => {
    Speech.stop();
    console.log('stop');
  }

  const goHome = async () => {
    stop();
    navigation.goBack();
  };

  // function for summarizing 
  const summarize = async () => {
    stop();
    const sum = "We are summarizing now, Steven Wu!!";
    speak(sum);
  };

  useEffect(() => {
    speak(glasses);
  },[]);

  return (
    <View style={{ flex: 1 }}>
      <Pressable style={styles.pressing} onPress={paused ? resume : pause}>
        <ImageBackground source={{ uri }} style={styles.image} resizeMode="contain"> 
          {progress ? (<AntDesign name="sound" style={styles.soundIcon} size={36} backgroundColor="#00000077" color="white" />) : undefined}
        </ImageBackground>
      </Pressable>
      <View style={styles.buttonContainer}>
        <TouchableOpacity style={styles.button} onPress={goHome}>
          <Ionicons name="close-outline" size={50} color="#fff" />
          <Text style={styles.buttonText}>Cancel</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={summarize}>
          <Ionicons name="checkmark-outline" size={50} color="#fff" />
          <Text style={styles.buttonText}>Summarize</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  buttonContainer: {
    position: "absolute",
    bottom: 0,
    left: 0,
    right: 0,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    zIndex: 1,
    height: "25%",
    backgroundColor: "#333",
  },
  button: {
    flex: 1,
    height: "100%",
    backgroundColor: "#333",
    justifyContent: "center",
    alignItems: "center",
  },
  buttonText: {
    color: "#fff",
    fontSize: 16,
    marginTop: 5,
    textAlign: "center",
  },
  image: {
    flex: 1,
    width: "100%",
    height: "100%",
  },
  pressing: {
    backgroundColor: "red",
    width: "100%",
    height: "100%",
  },
  soundIcon: {
    margin: 6,
    padding: 13,
    width: 62,
    height: 62,
    borderRadius: 62/2,
    overflow: 'hidden'
  }
});
