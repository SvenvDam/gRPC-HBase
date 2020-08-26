import Dependencies._

enablePlugins(AkkaGrpcPlugin)
enablePlugins(JavaAgent)

name := "server"

version := "0.1"

scalaVersion := "2.13.1"

libraryDependencies ++=
  common ++
    hBase ++
    akka ++
    logging :+
    scalatest

// protobuf stuff
javaAgents += "org.mortbay.jetty.alpn" % "jetty-alpn-agent" % "2.0.9" % "runtime;test"
PB.protoSources in Compile := Seq(file("../proto"))
libraryDependencies += "com.thesamet.scalapb" %% "scalapb-runtime" % scalapb
  .compiler
  .Version
  .scalapbVersion % "protobuf"

assemblyMergeStrategy in assembly := {
  case x if Assembly.isConfigFile(x) => MergeStrategy.concat
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case _                             => MergeStrategy.last
}
