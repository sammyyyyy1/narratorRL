import React, { useState, useEffect } from "react";
import { Image, StyleSheet, ImageBackground, View, TouchableOpacity, Text, Pressable, Animated, Switch } from "react-native";
import { Ionicons, AntDesign } from "@expo/vector-icons";
import * as Speech from 'expo-speech';
import env from "./env";

export default function Capture({ navigation, route }) {
  const [progress, setProgress] = useState(false);
  const [paused, setPaused] = useState(false);
  const [advanced, setAdvanced] = useState(false);
  const pauseAnim = React.useRef(new Animated.Value(0)).current;
  const playAnim = React.useRef(new Animated.Value(0)).current;
  const { id, text, uri } = route.params;

  const speak = (text) => {
    const start = () => {
      setProgress(true);
    };
    
    const finish = () => {
      setProgress(false);
      setPaused(false);
    }

    const options = {
      pitch: 1.0,
      rate: 1.0,
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
    Animated.sequence([
      Animated.timing(pauseAnim, {
        toValue: 1,
        duration: 500,
        useNativeDriver: true,
      }),
    ]).start(() => {});
  }

  const resume = () => {
    Speech.resume();
    setPaused(false);
    Animated.sequence([
      Animated.timing(playAnim, {
        toValue: 1,
        duration: 500,
        useNativeDriver: true,
      }),
      Animated.timing(playAnim, {
        toValue: 0,
        duration: 100,
        useNativeDriver: true,
      })
    ]).start(() => {});
  }

  const stop = () => {
    Speech.stop();
  }

  const goHome = async () => {
    stop();
    navigation.goBack();
  };

  const summarize = async () => {
    stop();
    const response = await fetch(`http://${env.ip}:8000/summarize/${id}`);
    const result  = await response.json();
    speak(result.text);
  };

  useEffect(() => {
    speak(text);
  },[]);

  const toggleSwitch = () => {
    setAdvanced(!advanced);
    console.log(advanced);
  };

  return (
    <View style={{ flex: 1 }}>
      <View style={styles.headerContainer}>
      {progress ? (<AntDesign name="sound" style={styles.progressIcon} size={36} backgroundColor="#00000077" color="white" />) : undefined}
          <View style={styles.contain}>
            <Pressable onPress={toggleSwitch} style={({pressed}) => [
              {
                backgroundColor: advanced ? '#5899f7' : '#00000077',
                borderColor: advanced ? '#5899f7' : '#00000077',
                top: "50%",
                right: "10%"
              },
              styles.textWrap
            ]}>
              <Text style={styles.switchText}>
                Advanced
              </Text>
            </Pressable>
          </View>
      </View>
      <Pressable style={styles.pressing} onPress={paused ? resume : pause}>
        <ImageBackground source={{ uri }} style={styles.image} resizeMode="contain"> 
          {paused ? 
          (<Animated.View style={[styles.soundIconWrapper, { opacity: pauseAnim }]}>
            <Ionicons name="pause-outline" style={styles.soundIcon} size={100} color="white" />
          </Animated.View>) 
          : (<Animated.View style={[styles.soundIconWrapper, { opacity: playAnim }]}>
            <Ionicons name="play" style={styles.soundIcon} size={100} color="white" />
          </Animated.View>)}
        </ImageBackground>
      </Pressable>
      <View style={styles.buttonContainer}>
        <TouchableOpacity style={styles.button} onPress={goHome}>
          <Ionicons name="close-outline" size={50} color="#fff" />
          <Text style={styles.buttonText}>Cancel</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={summarize}>
          <Ionicons name="reader-outline" size={50} color="#fff" />
          <Text style={styles.buttonText}>Summarize</Text>
        </TouchableOpacity>
        {advanced ? 
        (<TouchableOpacity style={styles.button} onPress={summarize}>
          <Ionicons name="ios-globe-outline" size={50} color="#fff" />
          <Text style={styles.buttonText}>Language</Text>
        </TouchableOpacity>) : undefined}
        {advanced ? 
        (<TouchableOpacity style={styles.button} onPress={summarize}>
          <Ionicons name="logo-closed-captioning" size={50} color="#fff" />
          <Text style={styles.buttonText}>Richard</Text>
        </TouchableOpacity>) : undefined}
      </View>
    </View>
  );
}
   

const styles = StyleSheet.create({
  headerContainer: {
    position: "absolute",
    top: 0,
    left: 0,
    right: 0,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    zIndex: 1,
    height: "15%",
  },
  headerImage: {
    flex: 1,
    top: "5%",
    left: "10%",
    right: "10%",
    height: "50%",
    width: "50%",
    justifyContent: "center",
  },
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
    backgroundColor: "#33333388",
  },
  button: {
    flex: 1,
    height: "100%",
    backgroundColor: "#33333388",
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
    alignContent: "center",
  },
  progressIcon: {
    margin: 6,
    padding: 13,
    width: 62,
    height: 62,
    borderRadius: 62/2,
    overflow: 'hidden',
    top: "5%",
    left: "5%"
  },
  soundIconWrapper: {
    position: "absolute",
    top: "30%",
    left: "40%",
    alignContent: "center",
    alignSelf:"center",
  },
  contain: {
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    position: 'absolute',
    top: 0,
    right: 0,
  },
  textWrap: {
    justifyContent: "center",
    alignItems: "center",
    borderWidth: 2,
    borderRadius: 15,
    overflow: 'hidden',
    height: 31,
    width: 95,
    marginTop: 19,
    marginRight: 6,    
  },
  switchText: {
    color: "white",
    fontWeight: 'bold',
    fontSize: 17,
  }
});
