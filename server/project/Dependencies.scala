import sbt._

object Dependencies {
  val hBaseVersion = "2.2.0"
  val hadoopVersion = "2.8.5"
  val akkaStreamVersion = "2.6.3"

  lazy val common = Seq(
    "com.typesafe" % "config" % "1.3.3",
    "io.grpc" % "grpc-netty-shaded" % "1.25.0"
  )

  lazy val hBase = Seq(
    "org.apache.hbase" % "hbase-client" % hBaseVersion,
    "org.apache.hadoop" % "hadoop-common" % hadoopVersion,
    "org.apache.hbase" % "hbase-server" % hBaseVersion,
    "org.apache.hadoop" % "hadoop-hdfs" % hadoopVersion,
    "org.apache.hbase" % "hbase-hadoop-compat" % hBaseVersion,
    "org.apache.hbase" % "hbase-hadoop2-compat" % hBaseVersion,
    "org.apache.hbase" % "hbase-testing-util" % hBaseVersion
  )

  lazy val logging = Seq(
    "com.typesafe.scala-logging" %% "scala-logging" % "3.9.2",
    "ch.qos.logback" % "logback-classic" % "1.2.3"
  )

  lazy val akka = Seq(
    "com.typesafe.akka" %% "akka-discovery" % akkaStreamVersion,
    "com.typesafe.akka" %% "akka-stream" % akkaStreamVersion,
    "com.typesafe.akka" %% "akka-stream-testkit" % akkaStreamVersion % Test
  )

  lazy val scalatest = "org.scalatest" %% "scalatest" % "3.0.8"
}
