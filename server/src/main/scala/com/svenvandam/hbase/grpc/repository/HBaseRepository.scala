package com.svenvandam.hbase.grpc.repository

import com.svenvandam.hbase.grpc.proto.Table
import org.apache.hadoop.hbase.TableName
import org.apache.hadoop.hbase.client._
import scala.concurrent.{blocking, ExecutionContext, Future}

class HBaseRepository(conn: Connection, context: ExecutionContext) {
  implicit val ec = context

  def get(get: => Get, table: Table): Future[Result] = Future {
    blocking {
      conn.getTable(TableName.valueOf(table.namespace, table.name)).get(get)
    }
  }

  def scan(scan: => Scan, table: Table): Future[ResultScanner] = Future {
    blocking {
      conn.getTable(TableName.valueOf(table.namespace, table.name)).getScanner(scan)
    }
  }

  def put(put: Put, table: Table): Future[Unit] = Future {
    blocking {
      conn.getTable(TableName.valueOf(table.namespace, table.name)).put(put)
    }
  }

  def delete(delete: Delete, table: Table): Future[Unit] = Future {
    blocking {
      conn.getTable(TableName.valueOf(table.namespace, table.name)).delete(delete)
    }
  }
}
