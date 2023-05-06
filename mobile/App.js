import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import Home from "./Home";
import Capture from "./Capture";

const Stack = createStackNavigator();

const headerStyle = {
    headerTintColor: '#fff',
    headerStyle: {
      backgroundColor: '#333',
      borderBottomWidth: 0,
      height: 100,
    },
    headerTitleStyle: {
      fontSize: 30,
    },
  };

  const App = () => {
    return (
      <NavigationContainer>
        <Stack.Navigator
          initialRouteName="narratorRL"
          screenOptions={headerStyle}
        >
          <Stack.Screen name="narratorRL" component={Home} />
          <Stack.Screen
            name="Capture"
            component={Capture}
            options={{
              headerLeft: null,
            }}
          />
        </Stack.Navigator>
      </NavigationContainer>
    );
  };
  
  export default App;
