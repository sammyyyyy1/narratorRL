import React, { useState, useEffect } from "react";
import { StyleSheet, ImageBackground, View, TouchableOpacity, Text, Pressable, Animated, Switch } from "react-native";
import { Ionicons, AntDesign } from "@expo/vector-icons";
import * as Speech from 'expo-speech';

export default function Capture({ navigation, route }) {
  const [progress, setProgress] = useState(false);
  const [paused, setPaused] = useState(false);
  const [advanced, setAdvanced] = useState(false);
  const pauseAnim = React.useRef(new Animated.Value(0)).current;
  const playAnim = React.useRef(new Animated.Value(0)).current;
  const { uri, text } = route.params;

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
    const sum = "We are summarizing now, Steven Wu!!";
    speak(sum);
  };

  useEffect(() => {
    speak(text);
  },[]);

  const toggleSwitch = () => setAdvanced(previousState => !previousState);

  return (
    <View style={{ flex: 1 }}>
      <Pressable style={styles.pressing} onPress={paused ? resume : pause}>
        <ImageBackground source={{ uri }} style={styles.image} resizeMode="contain"> 
          {progress ? (<AntDesign name="sound" style={styles.progressIcon} size={36} backgroundColor="#00000077" color="white" />) : undefined}
          <View style={styles.contain}>
            <View style={styles.textWrap}>
              <Text style={styles.switchText}>
                Advanced
              </Text>
            </View>
            <Switch 
              trackColor={{ false: "#767577", true: "#ffffff" }}
              thumbColor={advanced ? "#5899f7" : "#f4f3f4"}
              onValueChange={toggleSwitch}
              value={advanced}
              style={styles.switch}
            />
          </View>
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
    alignContent: "center",
  },
  progressIcon: {
    margin: 6,
    padding: 13,
    width: 62,
    height: 62,
    borderRadius: 62/2,
    overflow: 'hidden'
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
  switch: {
    marginLeft: 5,
    margin: "5%",
  },
  textWrap: {
    justifyContent: "center",
    alignItems: "center",
    borderWidth: 2,
    borderRadius: 15,
    overflow: 'hidden',
    height: 31,
    width: 95,
    backgroundColor: '#00000077',
    borderColor: '#00000077',    
  },
  switchText: {
    color: "white",
    fontWeight: 'bold',
    fontSize: 17,
  }
});
