#include <Arduino.h>

#include <finite_state_machine.hpp>

// Include all states

// Include communication headers
#include <message_handlers/RemoteTestSiteBasestation.hpp>
#include <comunication_devices/usr_lg206_p_adapter.hpp>
#include <proto_handlers/proto_handler.hpp>
#include <connection_handler.hpp>

RemoteTestSiteBasestation message_handler = RemoteTestSiteBasestation();

UsrLg206PAdapter communication_device = UsrLg206PAdapter();

ProtoHelper proto_helper = ProtoHelper();
ProtoHandler proto_handler = ProtoHandler(&proto_helper);

ConnectionHandler handler = ConnectionHandler(&message_handler, &communication_device, &proto_handler);

void setup()
{
  Serial.begin(9600);
  Serial1.begin(115200);
  message_handler.SetConnectionHandler(&handler);

  Serial.println("Basisstation is starting");

  while (!handler.Begin())
  {
    Serial.println("LoRa is not starting");
    delay(1000);
  }
}

void loop()
{
  // put your main code here, to run repeatedly:
  if (handler.Available())
  {
    handler.Read();
  }
}
