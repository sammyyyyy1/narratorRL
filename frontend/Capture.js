import React from "react";
import { StyleSheet, Image, View, TouchableOpacity, Text } from "react-native";
import { Ionicons } from "@expo/vector-icons";



export default function Capture({ navigation, route }) {
  const { uri } = route.params;

  const goHome = async () => {
    navigation.goBack();
  };

  const readPicture = async () => {};

  return (
    <View style={{ flex: 1 }}>
      <Image source={{ uri }} style={styles.image} resizeMode="contain" />
      <View style={styles.buttonContainer}>
        <TouchableOpacity style={styles.button} onPress={goHome}>
          <Ionicons name="close-outline" size={50} color="#fff" />
          <Text style={styles.buttonText}>Cancel</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={readPicture}>
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
});
