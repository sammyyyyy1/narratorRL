import React, { useState, useEffect, useRef } from "react";
import { Image, StyleSheet, View, Text, TouchableOpacity } from "react-native";
import { Camera } from "expo-camera";
import { Ionicons } from "@expo/vector-icons";
import * as FileSystem from "expo-file-system";
import * as ImageManipulator from 'expo-image-manipulator';
import env from "./env";

export default function Home({ navigation }) {
  const [hasPermission, setHasPermission] = useState(null);
  const [flashOn, setFlashOn] = useState(false);
  const cameraRef = useRef(null);

  useEffect(() => {
    (async () => {
      const { status } = await Camera.requestCameraPermissionsAsync();
      setHasPermission(status === "granted");
    })();
  }, []);

  const takePicture = async () => {
    if (cameraRef.current) {
      const { uri } = await cameraRef.current.takePictureAsync();
      const manip = await ImageManipulator.manipulateAsync(
        uri, [ {rotate: -360} ]);
      console.log(manip);
      const based64 = await FileSystem.readAsStringAsync(manip.uri, { encoding: FileSystem.EncodingType.Base64 });
      const base64 = based64.replaceAll('/', ';');
      console.log(base64.length);

      const response = await fetch(`http://${env.ip}:8000/read/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          image: base64,
        }),
      });
      const result  = await response.json();
      console.log(result);

      // const data = await response.json();
      // console.log(data);

      const dir = FileSystem.documentDirectory + "photos/";
      await FileSystem.makeDirectoryAsync(dir, { intermediates: true });
      const filename = new Date().getTime() + ".jpg";
      const path = dir + filename;

      await FileSystem.moveAsync({ from: uri, to: path });

      navigation.navigate("Capture", { uri: path, ...result });
    }
  };

  const toggleFlash = () => {
    setFlashOn(!flashOn);
  };

  if (hasPermission === null) {
    return <View />;
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>;
  }

  return (
    <View style={{ flex: 1 }}>
      <View style={styles.headerContainer}>
        <Image
          style={styles.headerImage}
          resizeMode="contain"
          source={require('./assets/logo.png')}
        />
      </View>
      <Camera
        style={{ flex: 1 }}
        type={Camera.Constants.Type.back}
        flashMode={
          flashOn
            ? Camera.Constants.FlashMode.torch
            : Camera.Constants.FlashMode.off
        }
        ref={cameraRef}
      />
      <View style={styles.buttonContainer}>
        <TouchableOpacity style={styles.button} onPress={takePicture}>
          <Ionicons name="camera" size={50} color="#fff" />
          <Text style={styles.buttonText}>Take Picture</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={toggleFlash}>
          <Ionicons name="flashlight" size={50} color="#fff" />
          <Text style={styles.buttonText}>
            {flashOn ? "Flash Off" : "Flash On"}
          </Text>
        </TouchableOpacity>
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
    backgroundColor: "#33333388",
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
});
