import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { setIsNewGroup, setIsNotification } from "../reducers/misc";


function MiscComponent() {
  // 1. Read state from Redux store
  const isNewGroup = useSelector((state) => state.misc.isNewGroup);
  const isNotification = useSelector((state) => state.misc.isNotification);

  // 2. Get dispatch function
  const dispatch = useDispatch();

  return (
    <div>
      <h2>isNewGroup: {isNewGroup ? "True" : "False"}</h2>
      <h2>isNotification: {isNotification ? "On" : "Off"}</h2>

      {/* 3. Dispatch actions to update state */}
      <button onClick={() => dispatch(setIsNewGroup(true))}>
        Enable New Group
      </button>
      <button onClick={() => dispatch(setIsNotification(!isNotification))}>
        Toggle Notification
      </button>
    </div>
  );
}

export default MiscComponent;
