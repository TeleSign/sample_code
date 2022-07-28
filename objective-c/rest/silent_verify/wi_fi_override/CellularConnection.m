#include <arpa/inet.h>
#include <net/if.h>
#import <netdb.h>
#include <netinet/in.h>
#include <regex.h>
#include <sys/types.h>
#import "CellularPlugin.h"
 
@implementation CellularPlugin
+ (void)registerWithRegistrar:(NSObject<FlutterPluginRegistrar> *)registrar {
  FlutterMethodChannel *channel =
      [FlutterMethodChannel methodChannelWithName:@"cellular"
                                  binaryMessenger:[registrar messenger]];
  CellularPlugin *instance = [[CellularPlugin alloc] init];
  [registrar addMethodCallDelegate:instance channel:channel];
}
 
- (void)handleMethodCall:(FlutterMethodCall *)call
                  result:(FlutterResult)result {
  NSString *url = call.arguments[@"url"];
  NSString *method = call.arguments[@"method"];
  NSString *data = call.arguments[@"payload"];
 
  if ([@"sendRequest" isEqualToString:call.method]) {
    NSString *response = [self sendRequest:url method:method data:data];
    result(response);
  } else {
    result(FlutterMethodNotImplemented);
  }
}
 
- (NSString *)sendRequest:(NSString *)url
                   method:(NSString *)method
                     data:(NSString *)data {
  NSString *domain = @"";
  NSString *resource = @"/";
 
  NSString *searchedString = url;
  NSRange searchedRange = NSMakeRange(0, [searchedString length]);
  NSString *pattern = @"(.*:)\\/\\/([A-Za-z0-9\\-\\.]+)(:[0-9]+)?(.*)";
  NSError *error = nil;
 
  NSRegularExpression *regex =
      [NSRegularExpression regularExpressionWithPattern:pattern
                                                options:0
                                                  error:&error];
  NSArray *matches = [regex matchesInString:searchedString
                                    options:0
                                      range:searchedRange];
 
  for (NSTextCheckingResult *match in matches) {
    NSString *matchText = [searchedString substringWithRange:[match range]];
    NSLog(@"match: %@", matchText);
    NSRange matchUrl = [match rangeAtIndex:0];
    NSRange matchProtocol = [match rangeAtIndex:1];
    NSRange matchDomain = [match rangeAtIndex:2];
    NSRange matchResource = [match rangeAtIndex:4];
 
    if (matchDomain.length > 0) {
      domain = [searchedString substringWithRange:matchDomain];
    }
 
    if (matchResource.length > 0) {
      resource = [searchedString substringWithRange:matchResource];
    }
  }
 
  // Retrieves the index of the "pdp_ip0" which is usually the cellular adapter
  int index = if_nametoindex("pdp_ip0");
 
  const char *charUrl = [domain UTF8String];
  struct hostent *target;
  target = gethostbyname(charUrl);
 
  if (target == NULL) {
    NSLog(@"Error getting domain info");
    return @"Error getting domain info";
  }
 
  if ([method isEqualToString:@"POST"]) {
    method = @"POST ";
  } else {
    method = @"GET ";
  }
 
  NSUInteger length = [data length];
 
  const char *payload = [[NSString
      stringWithFormat:
          @"%@%@%@%@%@%@%@%@%@", method, resource, @" HTTP/1.1\r\nHost: ",
          domain, @"\r\nUser-Agent: PostmanRuntime/7.26.10\r\nContent-Length: ",
          [NSString stringWithFormat:@"%tu", length],
          @"\r\nContent-Type:application/json\r\n\r\n", data, @"\r\n"]
      UTF8String];
 
  struct sockaddr_in myaddr;
 
  // Create the socket
  int socketNumber;
  socketNumber = socket(AF_INET, SOCK_STREAM, 0);
 
  if (socketNumber == -1) {
    NSLog(@"Error making socket");
  }
 
  // Bind socket to &index, which should be the cellular network connection
  int success =
      setsockopt(socketNumber, IPPROTO_IP, IP_BOUND_IF, &index, sizeof(index));
  if (success != 0) {
    NSLog(@"Error binding socket to Cellular");
    return @"Error binding socket to Cellular";
  }
 
  myaddr.sin_port = htons(80);
  memset(&myaddr.sin_zero, '\0', 8);
 
  struct in_addr **addr_list;
  addr_list = (struct in_addr **)target->h_addr_list;
 
  struct sockaddr_in dest;
 
  dest.sin_family = AF_INET;
  dest.sin_port = htons(80);
  NSLog(@"%s", payload);
  dest.sin_addr.s_addr = inet_addr(inet_ntoa(*addr_list[0]));
 
  int connectResult =
      connect(socketNumber, (struct sockaddr *)&dest, sizeof(struct sockaddr));
 
  if (connectResult == -1) {
    NSLog(@"Error connecting");
    return @"Connection Error";
  }
 
  int sendResult = sendto(socketNumber, payload, strlen(payload), 0,
                          (struct sockaddr *)&dest, sizeof(struct sockaddr));
 
  if (sendResult == -1) {
    NSLog(@"Sendind failed");
    return @"Sending failed";
  }
 
  int byteCount;
  socklen_t fromlen;
  struct sockaddr_storage addr;
  static char buf[65507];
  NSString *response = @"";
 
  fromlen = sizeof addr;
  byteCount = recvfrom(socketNumber, buf, sizeof buf, 0,
                       (struct sockaddr *)&addr, &fromlen);
 
  response = [NSString stringWithFormat:@"%s", buf];
 
  return response;
}
 
@end